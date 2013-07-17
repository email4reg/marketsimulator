from marketsim import ops, types, event, _, getLabel, Event

import fold
import blist

class Min(fold.Last, ops.Observable[float]):
    
    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self.timeframe = timeframe
        self.reset()
        
    _properties = { 'timeframe' : float }
        
    def reset(self):
        self._levels = blist.sorteddict()
        self._x = None
    
    def at(self, t):
        p = self._levels.keys()[0] if len(self._levels) > 0 else None
        x = self._x
        if p is not None:
            if x is not None:
                return min(p,x)
            return p
        return x
         
    def _getLabel(self):
        return 'Min_{%s}' % self.timeframe

    def _remove(self, x):
        self._levels[x] -= 1
        if self._levels[x] == 0:
            del self._levels[x]
        self.fire(self)
    
    def update(self, t, x):
        if x is not None and (self._x is None or x < self._x):
            if x not in self._levels:
                self._levels[x] = 0
            self._levels[x] += 1 
            self._scheduler.scheduleAfter(self.timeframe, _(self, x)._remove)
        self._x = x
        self.fire(self)
        
class Max(fold.Last, ops.Observable[float]):
    
    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self.timeframe = timeframe
        self.reset()
        
    _properties = { 'timeframe' : float }
        
    def reset(self):
        self._levels = blist.sorteddict()
        self._x = None
    
    def at(self, t):
        p = -self._levels.keys()[0] if len(self._levels) > 0 else None
        x = self._x
        if p is not None:
            if x is not None:
                return max(p,x)
            return p
        return x
         
    def _getLabel(self):
        return 'Max_{%s}' % self.timeframe

    def _remove(self, x):
        self._levels[-x] -= 1
        if self._levels[-x] == 0:
            del self._levels[-x]
        self.fire(self)
    
    def update(self, t, x):
        if x is not None and (self._x is None or x > self._x):
            if -x not in self._levels:
                self._levels[-x] = 0
            self._levels[-x] += 1 
            self._scheduler.scheduleAfter(self.timeframe, _(self, x)._remove)
        self._x = x
        self.fire(self)
        
    
    