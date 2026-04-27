class Portfolio:
    def __init__(self):
        self.cash = 1000
        self.stock = 0
        
    def buy(self, shares, price):
        cost = shares * price
        if cost <= self.cash:
            self.cash -= cost
            self.stock += shares
            print(f"Bought {shares} shares")
        else:
            print(f"Need ${cost}, only have ${self.cash}")
            
            
    def sell(self, shares, price):
        if shares <= self.stock:
            self.cash += shares * price
            self.stock -= shares
            print(f"Sold {shares} shares")
        else:
            print(f"Only have {self.stock} shares")
            
    def value(self, current_price):
        return self.cash + (self.stock * current_price)
    
    
if __name__ == "__main__":
    p = Portfolio()
    p.buy(10, 100)
    print(f"Cash left: ${p.cash}")
    p.sell(5, 110)
    print(f"Portfolio value: ${p.value(115)}")