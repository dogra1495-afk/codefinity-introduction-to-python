produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce] + [dairy]

for section in groceries:
    print(groceries)
    for item in section:
        print(F"Item name: {item}")
    








