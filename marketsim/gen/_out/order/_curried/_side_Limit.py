from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class side_Limit(IFunction[IOrderGenerator, IFunction[Side]
]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, price = None, volume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.price = price if price is not None else _constant(100.0)
        self.volume = volume if volume is not None else _constant(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunction[float],
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "side_Limit(%(price)s, %(volume)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.order._Limit import Limit
        side = side if side is not None else _side_Sell()
        price = self.price
        volume = self.volume
        return Limit(side, price, volume)
    
