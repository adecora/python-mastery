# tableformat.py
from abc import ABC, abstractmethod
import sys


def print_table(portfolio, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')  
      
    formatter.headings(fields)
    for s in portfolio:
        rowdata = [getattr(s, fieldname, None) for fieldname in fields]
        formatter.row(rowdata)


class TableFormatter(ABC):
    _formats = {}

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeaderMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file
    
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout    


def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)
    
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats
    
    if upper_headers:
        class formatter_cls(UpperHeaderMixin, formatter_cls):
            pass

    return formatter_cls()
