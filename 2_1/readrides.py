# readrides.py

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
            datatype = row[2]
            rides = int(row[3])
            record = (route, date, datatype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            datatype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'datatype': datatype,
                'rides': rides
            }
            records.append(record)
    return records

class Row:
    # Uncomment to see effect of slots
    __slots__ = ('route', 'date', 'datatype', 'rides')
    def __init__(self, route, date, datatype, rides):
        self.route = route
        self.date = date
        self.datatype = datatype
        self.rides = rides

# Uncomment to use namedtuple instead
# option A
# from collections import namedtuple
# Row = namedtuple('Row', ('route', 'date', 'datatype', 'rides'))
# option B
# import typing
# class Row(typing.NamedTuple):
    # route: str
    # date: str
    # datatype: str
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
            datatype = row[2]
            rides = row[3]
            record = Row(route, date, datatype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import sys
    import tracemalloc
    if len(sys.argv) != 2:
        raise SystemExit('Usage: readrides.py (tuple|dict|instance)')
    options = {
        'tuple': read_rides_as_tuples,
        'dict': read_rides_as_dicts,
        'instance': read_rides_as_instances
     }
    tracemalloc.start()
    read_rides = options.get(sys.argv[1])
    rows = read_rides('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
