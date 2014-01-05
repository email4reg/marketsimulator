from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class pricevolume_WithExpiry(IFunction[IOrderGenerator, IFunction[float],IFunction[float]
]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._curried._pricevolume_Limit import pricevolume_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else pricevolume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float],IFunction[float]
        ]
    }
    def __repr__(self):
        return "pricevolume_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None,volume = None):
        from marketsim.gen._out.order._WithExpiry import WithExpiry
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(price,volume))
    