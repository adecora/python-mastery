# structure.py

from validate import Validator, validated
from collections import ChainMap


def validate_attributes(cls):
    '''
    Class decorator that scans a class definition for Vaidators
    and builds a _fields variable that captures their definition order.
    '''
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        
        # Apply validated decorator to any callable with annotations
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    # Collect all of the field names
    cls._fields = tuple([val.name for val in validators])

    # Collect type conversions. The lambda x:xis an identity
    # function that's used in case no expected_type is found.
    cls._types = tuple([getattr(val, 'expected_type', lambda x: x) 
                    for val in validators])
    
    # Create the __init__ method
    if cls._fields:
        cls.create_init()
    
    return cls

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)
    
    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
    _types = ()
    _fields = ()
    
    def __setattr__(self, name, value):
        if name in self._fields or name.startswith('_'):
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        args = ','.join(cls._fields)
        code = f'def __init__(self, {args}):\n'
        for name in cls._fields:
            code += f'   self.{name} = {name}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']
    
    @classmethod
    def __init_subclass__(cls):
        # Apply the validated decorator to subclasses
        validate_attributes(cls)


def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure, ), validators)
    return cls