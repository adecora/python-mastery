# reader.py

import collections.abc
import csv


def read_csv_as_dicts(filename, coltypes):
    result = list()
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, coltypes, row) }
            result.append(record)
    return result


class DataCollection(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all the value (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All list assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            cls = DataCollection()
            cls.routes = self.routes[index]
            cls.dates = self.dates[index]
            cls.daytypes = self.daytypes[index]
            cls.numrides = self.numrides[index]
            return cls
        else:
            return { 'route': self.routes[index],
                     'date': self.dates[index],
                     'daytype': self.daytypes[index],
                     'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


def read_csv_as_columns(filename, coltypes):
    result = DataCollection()
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, coltypes, row) }
            result.append(record)
    return result


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

