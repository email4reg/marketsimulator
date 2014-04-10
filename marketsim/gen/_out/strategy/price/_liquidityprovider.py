# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["-", "LiquidityProvider"])
class LiquidityProvider_FloatFloatIOrderBook(object):
    """ 
    """ 
    def __init__(self, initialValue = None, priceDistr = None, book = None):
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate_FloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import rtti
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else deref_opt(_math_random_lognormvariate_FloatFloat(0.0,0.1))
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'initialValue' : float,
        'priceDistr' : IFunctionfloat,
        'book' : IOrderBook
    }
    
    
    
    
    
    
    def __repr__(self):
        return "LiquidityProvider(%(initialValue)s, %(priceDistr)s, %(book)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.priceDistr.bind_ex(self._ctx_ex)
        self.book.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    

    @property
    def PriceDistr(self):
        from marketsim.gen._out.strategy.price._pricedistr import PriceDistr
        return PriceDistr(self)
    
    def Price(self, side = None):
        from marketsim.gen._out.strategy.price._price import Price
        return Price(self,side)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.price._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Book(self):
        from marketsim.gen._out.strategy.price._book import Book
        return Book(self)
    
    def OneSideStrategy(self, eventGen = None,orderFactory = None,side = None):
        from marketsim.gen._out.strategy.price._onesidestrategy import OneSideStrategy
        return OneSideStrategy(self,eventGen,orderFactory,side)
    
    @property
    def InitialValue(self):
        from marketsim.gen._out.strategy.price._initialvalue import InitialValue
        return InitialValue(self)
    
    pass
LiquidityProvider = LiquidityProvider_FloatFloatIOrderBook
