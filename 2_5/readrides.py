# readrides.py

import collections.abc
import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytape = row[2]
            rides = int(row[3])
            record = (route, date, daytape, rides)
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all the value (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            cls = RideData()
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

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytape = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytape,
                'rides': rides
            }
            records.append(record)
    return records


class Row:
    # Uncomment to see effect of slots
    __slots__ = ('route', 'date', 'daytape', 'rides')
    def __init__(self, route, date, daytape, rides):
        self.route = route
        self.date = date
        self.daytape = daytape
        self.rides = rides

# Uncomment to use namedtuple instead
# option A
# from collections import namedtuple
# Row = namedtuple('Row', ('route', 'date', 'daytape', 'rides'))
# option B
# import typing
# class Row(typing.NamedTuple):
    # route: str
    # date: str
    # daytape: str
    # rides: int

def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headings
        for row in rows:
            route = row[0]
            date = row[1]
            daytape = row[2]
            rides = row[3]
            record = Row(route, date, daytape, rides)
            records.append(record)
    return records


def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
