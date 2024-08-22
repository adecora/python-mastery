# follow.py
import os
import time


def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    with open(filename) as f:
        f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)  # Sleep briefly and retry
                continue
            yield line


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: follow.py filename")
    filename = sys.argv[1]
    for line in follow(filename):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
                print('%10s %10.2f %10.2f' % (name, price, change))
