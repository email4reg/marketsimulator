# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.suspendable import Suspendable_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Strategy", "Suspendable"])
class Suspendable_ISingleAssetStrategyBoolean(ISingleAssetStrategy,Suspendable_Impl):
    """ **Strategy that wraps another strategy and passes its orders only if *predicate* is true**
    
    
    Parameters are:
    
    **inner**
    	 wrapped strategy 
    
    **predicate**
    	 predicate to evaluate 
    """ 
    def __init__(self, inner = None, predicate = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        self.predicate = predicate if predicate is not None else deref_opt(_true_())
        rtti.check_fields(self)
        Suspendable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'predicate' : IFunctionbool
    }
    
    
    
    
    def __repr__(self):
        return "Suspendable(%(inner)s, %(predicate)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.inner.bind_ex(self._ctx_ex)
        self.predicate.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Suspendable(inner = None,predicate = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if predicate is None or rtti.can_be_casted(predicate, IFunctionbool):
            return Suspendable_ISingleAssetStrategyBoolean(inner,predicate)
    raise Exception('Cannot find suitable overload for Suspendable('+str(inner) +':'+ str(type(inner))+','+str(predicate) +':'+ str(type(predicate))+')')
