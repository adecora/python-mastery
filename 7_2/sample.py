# sample.py
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    return x * y
