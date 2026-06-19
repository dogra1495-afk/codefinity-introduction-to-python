prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = [0.10, 0.20, 0.15, 0.05,]

for i in range(len(prices)):
    new_price = prices[i] * (1 - discount_factor[i])
    prices[i] = new_price
    print(f"Updated price for item {i}: ${new_price:.2f}")


    








