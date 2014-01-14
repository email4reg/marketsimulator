from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _True_Impl
@registry.expose(["Basic", "true"])
class true(Function[bool], _True_Impl):
    """ 
    """ 
    def __init__(self):
        
        _True_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "True" % self.__dict__
    