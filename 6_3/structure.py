# structure.py

class Structure:
    _fields = ()
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    
    def __setattr__(self, name, value):
        if name in self._fields or name.startswith('_'):
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        code = f'def __init__(self, {args}):\n'
        for name in cls._fields:
            code += f'   self.{name} = {name}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']