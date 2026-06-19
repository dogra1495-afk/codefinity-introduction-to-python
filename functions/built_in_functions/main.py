# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
    price, quantity_sold = products[item]
    price_converted = float(price)
    quantity_sold_converted = int(quantity_sold)
    total_sales = quantity_sold_converted * price_converted
    total_sales_list.append(total_sales)
    print(F"Total sales for {item}: ${total_sales}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)


print(F"Total sum of all sales: ${total_sum}")
print(F"Minimum sales: ${min_sales}")
print(F"Maximum sales: ${max_sales}")




