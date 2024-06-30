# reader.py
import csv
from typing import Callable, Iterable, List, Optional, Type, TypeVar

T = TypeVar('T')

def csv_as_dicts(lines: Iterable, types: List[Callable], *, headers: Optional[List[str]] = None) -> List[dict]:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record  = { name: func(val) 
                    for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterable, cls: Type[T], *, headers: Optional[List[str]] = None) -> List[Type[T]]:
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_as_csv_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)