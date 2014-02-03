from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.cma import CMA_Impl
from marketsim import IObservable
from marketsim import IObservable
@registry.expose(["Statistics", "Avg"])
class Avg(Function[float], CMA_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        rtti.check_fields(self)
        CMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
    }
    def __repr__(self):
        return "Avg_{cumul}(%(source)s)" % self.__dict__
    
