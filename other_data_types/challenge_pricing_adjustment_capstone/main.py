grocery_inventory  = {
    "Milk": ("Dairy", 3.5, 8),
    "Eggs": ("Dairy", 5.5, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.5, 50),
}

category, price, stock = grocery_inventory["Eggs"]

if price > 5:
    new_price = price - 1
    print("Eggs are too expensive, reducing the price by $1.")
else:
    new_price = price
    print("The price of Eggs is reasonable.")
    
grocery_inventory["Eggs"] = (category, new_price, stock)

grocery_inventory["Tomatoes"] = ("Produce", 1.2, 30)

print(F"Inventory after adding Tomatoes: {grocery_inventory}")

category, price, stock = grocery_inventory["Milk"]

if stock < 10:
    new_stock = stock + 20
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    new_stock = stock
    print("Milk has sufficient stock.")

grocery_inventory["Milk"] = (category, price, new_stock)

category, price, stock = grocery_inventory["Apples"]

if price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(F"Updated inventory: {grocery_inventory}")











