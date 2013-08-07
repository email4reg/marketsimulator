import sys
sys.path.append(r'../..')

from marketsim import (Side, mathutils, parts, signal, strategy, observable, ops, order, scheduler)
from common import expose

class InterlacingSide(ops.Function[Side]):
    
    def __init__(self, phase = 1, timeframe = 10):
        self.timeframe = timeframe
        self.phase = phase
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        return Side.Buy \
                 if int(self._scheduler.currentTime / self.timeframe) % 2 == self.phase else \
               Side.Sell 

@expose("Various Orders", __name__)
def Orders(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    midPrice = observable.MidPrice(ctx.book_A)

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(5)), "liquidity"),
        
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Market(
                                side = parts.side.Signal(linear_signal), 
                                volume = const(1))), 
                         "signalmarket"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.StopLoss(
                                side = parts.side.Signal(linear_signal), 
                                volume = const(1),
                                maxloss = const(0.1))), 
                         "signalstoploss"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = parts.side.Signal(linear_signal), 
                                price = midPrice, 
                                volume = const(1))), 
                         "signallimit"), 
  
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = parts.side.Random(), 
                                price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                volume = const(1)),
                            scheduler.Timer(const(1))), 
                         "noiselimitmarket"), 
  
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                const(100), 
                                order.factory.Limit(
                                    side = parts.side.Random(), 
                                    price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                    volume = const(1))),
                            scheduler.Timer(const(1))), 
                         "noiselimitexpiry"), 
  
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.IcebergLimit(
                                side = parts.side.Random(), 
                                price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                volume = const(100),
                                lotsize = const(1)),
                            scheduler.Timer(const(100))), 
                         "noiseiceberglimit"), 
  
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.FixedBudget(
                                side = parts.side.Signal(linear_signal), 
                                budget = const(450))), 
                         "signalfixedbudget"), 
           
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.AlwaysBestLimit(
                                side = InterlacingSide(),
                                volume = const(10)),
                            scheduler.Timer(const(10))), 
                         "noise_alwaysbest"), 

        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                ops.constant(0.1),
                                order.factory.AlwaysBestLimit(
                                    side = InterlacingSide(),
                                    volume = const(10))),
                            scheduler.Timer(const(10))), 
                         "noise_alwaysbestexpiry"), 
    ]    
