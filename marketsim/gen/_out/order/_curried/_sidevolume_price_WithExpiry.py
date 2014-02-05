from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "WithExpiry"])
class sidevolume_price_WithExpiry(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
,IFunction[float]]):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim import IOrderGenerator
        from marketsim import float
        from marketsim import IFunction
        from marketsim import IFunction
        from marketsim import Side
        from marketsim import IFunction
        from marketsim import float
        from marketsim import IFunction
        from marketsim import IFunction
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        from marketsim import rtti
        IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
        ,IFunction[float]].__init__(self)
        self.expiry = expiry if expiry is not None else _constant(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunction[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._curried._price_WithExpiry import price_WithExpiry
        expiry = self.expiry
        proto = self.proto
        return price_WithExpiry(expiry, proto(side,volume))
    
sidevolume_price_WithExpiry = sidevolume_price_WithExpiry
