# logcall.py
from functools import wraps

def logged(func):
    print('Adding logging to', func.__name__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged


@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    return x * y


class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass
