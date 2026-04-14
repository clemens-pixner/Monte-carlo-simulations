import random

runs = 1000
annual_profits = []

quotes = {
    "loss_quote" : 0,
    "break_even_quote" : 0,
    "success_quote" : 0
}

def percentage_calc(quote, runs):
    percantage = (quote / runs) * 100
    return percantage
     
#Distribution
class TriangularDistribution:
    def __init__(self, min_val, max_val, mode): 
        self.min = min_val
        self.max = max_val
        self.mode = mode

    def sample(self):
        return random.triangular(self.min, self.max, self.mode)
    
#Values
class values:
    def __init__(self):
        #Variable costs
        self.purchase_price_margin = TriangularDistribution(0.60, 0.30, 0.45)
        self.selling_price = TriangularDistribution(0.80, 5.00, 2.50)
        self.products_sold = TriangularDistribution(300.0, 900.0, 600.0)
        #Fixed costs
        self.rent = 500.0
        self.maintanance = 150.0
        self.tax = 0.75

value = values()

for run in range(runs):
    annual_profit = 0.0

    for month in range(12):
        revenue = (value.selling_price * value.purchase_price_margin) * value.products_sold
        costs = value.rent + value.maintanance

        profit_before_tax = revenue - costs
        profit_after_tax = profit_before_tax * 0.75
        
        annual_profit += profit_after_tax

        if annual_profit < 0:
            quotes["loss_quote"] += 1
        elif annual_profit >= 0:
            quotes["break_even_quote"] += 1
        elif annual_profit >= 1000:
            quotes["success_quote"] += 1

    annual_profits.append(annual_profit)

avg_profit = sum(annual_profits) / len(annual_profits)
min_profit = min(annual_profits)
max_profit = max(annual_profits)

loss_percentage = percentage_calc(quotes["loss_quote"], runs)
break_even_percentage = percentage_calc(quotes["break_even_quote"], runs)
success_percentage = percentage_calc(quotes["success_quote"], runs)

print("\nProfit overview:")
print(f"Average profit: {avg_profit:.2f}€")
print(f"Minimul profit: {min_profit:.2f}€")
print(f"Maximum profit: {max_profit:.2f}€")
print("\nQuotes:")
print(f"Loss (-): {loss_percentage:.1f}% ({quotes["loss_quote"]}x)")
print(f"Break-even (0+): {break_even_percentage:.1f}% ({quotes["break_even_quote"]}x)")
print(f"Success (1000+): {success_percentage:.1f}% ({quotes["success_quote"]}x)")

