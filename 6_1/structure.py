# structure.py

class Structure:
    _fields = ()
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected %d arguments' % len(self._fields))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    
    def __setattr__(self, name, value):
        if name in self._fields or name.startswith('_'):
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
