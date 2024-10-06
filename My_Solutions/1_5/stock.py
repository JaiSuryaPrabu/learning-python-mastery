class Stock:
    def __init__(self,name,share,price):
        self.name = name
        self.share = share
        self.price = price

    def cost(self):
        return self.share * self.price
    
s = Stock("GOOG",100,490.1)

print(s.name)
print(s.share)
print(s.price)
print(s.cost())