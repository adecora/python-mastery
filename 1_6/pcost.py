# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                shares      = int(fields[1])
                price       = float(fields[2])
                total_cost += shares * price
            
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)

    return total_cost


if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))
