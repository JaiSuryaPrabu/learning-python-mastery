file_path = "E:/jai/docs/code/python/tutorial/learning-python-mastery/Data/portfolio.dat"

def portfolio_cost(filename : str) -> float:
    total_cost = 0
    with open(filename,mode='r') as file:
        for line in file:
            share_name,share_count,price = line.split()
            try:
                total_cost += (float(share_count) * float(price))
            except Exception as e:
                print(e)
    return total_cost

print(portfolio_cost(file_path))