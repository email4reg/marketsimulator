from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.moments.mv import MV_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "Var"])
class Var_IObservableFloatFloat(IFunctionfloat,MV_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import call
        from marketsim import rtti
        self.source = source if source is not None else call(_const_Float,1.0)
        self.timeframe = timeframe if timeframe is not None else 100.0
        rtti.check_fields(self)
        MV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "\\sigma^2_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
def Var(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Var_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for Var('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
