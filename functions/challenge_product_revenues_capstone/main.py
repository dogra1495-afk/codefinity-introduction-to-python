def calculate_revenue(prices, quantities_sold):
    revenue_list = []
    for i in range(len(prices)):
        revenue_list.append(prices[i] * quantities_sold[i])
    return revenue_list

def formatted_output(revenue_tuples):
    for name, rev in sorted(revenue_tuples):
        print(f"{name} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenues))

formatted_output(revenue_per_product)



# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")