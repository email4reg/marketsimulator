from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IObservableFloatIObservableFloat(Observable[bool],_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IFunctionFloatIObservableFloat(Observable[bool],_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IObservableFloatIFunctionFloat(Observable[bool],_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim import IFunction
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IFunctionFloatIFunctionFloat(Observable[bool],_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[bool].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        self.y = y if y is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
def GreaterEqual(x = None,y = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return GreaterEqual_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return GreaterEqual_IFunctionFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return GreaterEqual_IObservableFloatIFunctionFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return GreaterEqual_IFunctionFloatIFunctionFloat(x,y)
    raise Exception('Cannot find suitable overload for GreaterEqual('+str(x)+','+str(y)+')')
