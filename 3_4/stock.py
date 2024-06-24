# stock.py
from decimal import Decimal

class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares

    @property
    def price(self):
        return self._price

    @property
    def cost(self):
        return self.shares * self.price

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected a {self._types[1].__name__}')
        elif value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected a {self._types[2].__name__}')
        elif value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


class DStock(Stock):
    _types = (str, int, Decimal)
