from marketsim import trader, order, indicator, scheduler
from copy import copy

from _basic import Strategy

def createVirtual(constructor, kwargs):
    orderBook = kwargs['trader'].orderBook
    # to do something with labels
    kwargs['trader'] = trader.SASM(orderBook)
    kwargs['volumeDistr'] = lambda: 1
    kwargs['orderFactory'] = order.VirtualMarket.T 
    return constructor(*[], **kwargs)

def trend(source, alpha=0.015):
    return indicator.OnEveryDt(1, indicator.dEWMA(source, alpha))

def efficiency(trader):
    return indicator.TraderEfficiency([trader.on_traded], trader)

def withEstimator(constructor, *args, **kwargs): # todo: parametrize by efficiency criteria
    assert len(args) == 0, "positional arguments are not supported"
    estimator = createVirtual(constructor, copy(kwargs))
    real = constructor(*args, **kwargs)
    real.estimator = estimator 
    real.efficiency = trend(efficiency(estimator.trader))
    return real

def suspendIfNotEffective(strategy):    
    strategy.efficiency.on_changed += \
        lambda _: strategy.suspend(strategy.efficiency.value < 0)
    return strategy

class chooseTheBest(Strategy):

    def __init__(self, strategies, event_gen=None):
        assert all(map(lambda s: s.trader == strategies[0].trader, strategies))
        if event_gen is None:
            event_gen = scheduler.Timer(lambda: 1)
        Strategy.__init__(self, strategies[0].trader)
        self._strategies = strategies
        event_gen.advise(self._chooseTheBest)

    def _chooseTheBest(self, _):
        best = -10e38        
        for s in self._strategies:
            if s.efficiency.value > best:
                best = s.efficiency.value
        for s in self._strategies:
            s.suspend(best != s.efficiency.value)

    
    def suspend(self, s):
        Strategy.suspend(self, s)
        if not s:
            self._chooseTheBest(None)
        else:
            for s in self._strategies:
                s.suspend(True)