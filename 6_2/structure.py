# structure.py

import sys

class Structure:
    _fields = ()
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, value in locs.items():
            setattr(self, name, value)
    
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    
    def __setattr__(self, name, value):
        if name in self._fields or name.startswith('_'):
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
