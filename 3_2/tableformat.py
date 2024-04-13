# tableformat.py

def print_table(portfolio, attributes):
    for attr in attributes:
        print('%10s ' % attr, end='')
    print()
    print(('-'*10 + ' ')*len(attributes))
    for s in portfolio:
        for attr in attributes:
            print('%10s ' % getattr(s, attr, None), end='')
        print()

