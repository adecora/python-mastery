# pcost.py

def portfolio_cost(file):
    total = 0
    with open(file, 'r') as f:
        for line in f:
            try:
                fields = line.split()
                shares = int(fields[1])
                price = float(fields[2])
                total += shares * price
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
    return total


print(portfolio_cost('Data/portfolio3.dat'))
