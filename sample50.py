arr = [7,1,5,3,6,4]

min_price = float('inf')
max_profit = 0

for price in arr:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print(max_profit)