# pills.py
import time


def parse_line(line):
    res = line.split('=')
    if len(res) < 2:
        return None
    return res[0], res[1]

def worker(x, y):
    print('About to work')
    time.sleep(20)
    print('Done')
    return x + y
