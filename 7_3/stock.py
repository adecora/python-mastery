# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        print('self', self)
        return self.shares * self.price
    
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
