import inspect

class Strategy(object):
    
    def __init__(self, trader):
        self._suspended = False
        self._trader = trader
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s):
        self._suspended = s
        
    @property
    def trader(self):
        return self._trader

class TwoSides(Strategy):    
    
    def __init__(self, trader):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        
        Strategy.__init__(self, trader)
        
        # start listening calls from eventGen
        self._eventGen.advise(self._wakeUp)
        
    def dispose(self):
        self._eventGen.unadvise(self._wakeUp)

    def _wakeUp(self, signal):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        res = self._orderFunc()
        if res <> None:
            (side, params) = res
            # create order given side and parameters
            order = self._orderFactoryT(side)(*params)
            # send order to the order book
            self._trader.send(order)
        
class OneSide(Strategy):
    
    def __init__(self, trader):                
        """ Initializes generic one side trader and makes it working
        orderBook - book to place orders in
        side - side of orders to create
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> *orderParams 
        """     
        Strategy.__init__(self, trader)   
    
        # start listening calls from eventGen
        self._eventGen.advise(self._wakeUp)
        
    def dispose(self):
        self._eventGen.unadvise(self._wakeUp)

    def _wakeUp(self, signal):
        if self._suspended:
            return
        # determine parameters of an order to create
        params = self._orderFunc()
        # create an order with given parameters
        order = self._orderFactory(*params)
        # send the order to the order book
        self._trader.send(order)

class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]
            
currentframe = inspect.currentframe

class Wrapper(object):
    
    def __init__(self, ctor, properties):
                
        for k in properties:
            if k != 'self' and k != 'frame':
                self.__dict__[k] = properties[k]
                
        self._impl = None
        self._ctor = ctor
        
    @staticmethod
    def fromFrame(ctor, frame):
        _, _, _, values = inspect.getargvalues(frame)
        return Wrapper(ctor, dict(values))
    
    def clone(self):
        return Wrapper(self._ctor, self.__dict__)
    
    def cloneWith(self, **kwargs):
        return Wrapper(self._ctor, merge(self, **kwargs).__dict__)    
    
    def _respawn(self):
        if self._impl is not None:
            self._impl.dispose()
        self._impl = self._ctor(self._trader, self)
        
    def runAt(self, trader):
        assert self._impl is None, "a strategy can be bound to only one trader"
        self._trader = trader
        self._respawn()
        
    def __getattr__(self, item):
        if self._impl is not None:
            return getattr(self._impl, item)
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item[0] != '_':
            self._respawn()
    