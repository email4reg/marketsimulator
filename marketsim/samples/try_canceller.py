import sys
sys.path.append(r'../..')

from marketsim import (strategy, trader, orderbook, order, ops, Side, mathutils,
                       scheduler, observable, veusz, registry, timeserie)

from common import expose

@expose("Canceller", __name__)
def Canceller(ctx):

    ctx.volumeStep = 15

    return [
        ctx.makeTrader_A(strategy.LiquidityProviderSide(side = Side.Sell),
                         "LiquidityProvider-"),
        
        ctx.makeTrader_A(strategy.LiquidityProviderEx(
                            orderFactory=order.WithExpiryFactory(
                                    expirationDistr=ops.constant(1))),
                         "LiquidityProviderEx-"),
        
        ctx.makeTrader_A(strategy.LiquidityProvider2Ex(), "LiquidityProvider2"),
        
        ctx.makeTrader_A(strategy.LiquidityProviderSide2Ex(
                            side = Side.Sell, 
                            orderFactory = order.factory.SidePrice_Limit(
                                                volume = mathutils.rnd.expovariate(1.))),
                         "LiquidityProvider2Ex-"),
         
        ctx.makeTrader_A(strategy.LiquidityProviderSide(side = Side.Buy),
                         "LiquidityProviderBuy"),
    
        ctx.makeTrader_A(   strategy.Array([
                                strategy.LiquidityProviderSide(side = Side.Sell),
                                strategy.Canceller()
                            ]),
                           label = "LiquidityProviderWithCanceller"),
        
        ctx.makeTrader_A(  strategy.LiquidityProviderSide(
                                side = Side.Sell,
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=ops.constant(10))),
                           "LiquidityProviderWithExpiry"),
        
        ctx.makeTrader_A(   strategy.FundamentalValue(
                                fundamentalValue = ops.constant(1000)), 
                            "fv_1000")
        ]