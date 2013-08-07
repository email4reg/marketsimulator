from _limit import LimitFactory
from _meta import OwnsSingleOrder
from marketsim import request, meta, types, registry, bind, event, _, combine

class Volume(object):
    """ Auxiliary class to hold market order initialization parameters 
    """
    def __init__(self, v):
        self._volume = v

    hasPrice = False

    @property
    def packed(self):
        """ Returns a tuple (volume)"""
        return self._volume,

class PriceVolume(object):
    """ Auxiliary class to hold limit order initialization parameters 
    """

    def __init__(self, p, v):
        self._price = p
        self._volume = v

    hasPrice = True

    @property
    def packed(self):
        """ Returns a tuple (price, volume)"""
        return self._price, self._volume

def unpack(args):
    """ Unpacks from args volume (and possibly) price of order to create 
    """
    return PriceVolume(*args) if len(args) == 2 else Volume(*args)

class Iceberg(OwnsSingleOrder):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, orderFactory, *args):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        self._args = unpack(args)
        # we pretend that we are an order initially having given volume
        OwnsSingleOrder.__init__(self, None, self._args._volume, None)
        self._lotSize = lotSize
        self._orderFactory = orderFactory
        self._subscription = None
        self._side = None
        
    def onOrderMatched(self, order, price, volume):
        OwnsSingleOrder.onOrderMatched(self, order, price, volume)
        if order.empty:
            self._tryToResend()

    def _tryToResend(self):
        """ Tries to send a real order to the order bookCaC
        """
        # if we have something to trade
        if self.volumeUnmatched > 0: 
            # define volume to trade
            v = min(self._lotSize, self.volumeUnmatched)
            self._args._volume = v
            # create a real order
            self.send(self._orderFactory(*self._args.packed))
            self._side = self.order.side
        else:
            # now we have nothing to trade
            self.order = None

    def processIn(self, book):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self.orderBook = book
        self._tryToResend()
        
class FactoryLimit(types.IPersistentOrderGenerator, combine.SidePriceVolumeLotSize):
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        params = combine.SidePriceVolumeLotSize.__call__(self)
        if params is not None:
            (side, price, volume, lotsize) = params
            order = Iceberg(lotsize, LimitFactory(side), price, volume)
            return order
        return None
