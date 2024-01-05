# pcost.py

import sys

def computesum(portfolio):
    try:
        with open(portfolio, 'r') as f:
            total = 0
            for no, line in enumerate(f):
                fields = line.split()
                try:
                    shares = int(fields[1])
                    price = float(fields[2])
                    total += shares * price
                except ValueError:
                    print(f"Couldn't parse [{no}] {line}")
            print('Total =', total)
    except FileNotFoundError as e:
        print('File not found')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemError("Usage: pcost.py portfolio")
    computesum(sys.argv[1])
