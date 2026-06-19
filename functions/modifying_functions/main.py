def apply_discount(price = 120, discount=0.05):
    discount_price = price * (1 - discount)
    return discount_price



def apply_tax(price = 120, tax=0.07):
    tax_price = price * (1 + tax)
    return tax_price

def calculate_total(price=120, discount=0.05, tax=0.07):
    # 1) Apply discount to the `price` argument
    discounted_price = apply_discount(price, discount)
    # 2) Apply tax to the discounted amount
    total = apply_tax(discounted_price, tax)
    return total

total_price_default = calculate_total(price = 120, discount=0.05, tax=0.07)

print(F"Total cost with default discount and tax: ${total_price_default}")

total_price_custom = calculate_total(price = 100, discount=0.10, tax=0.08)

print(F"Total cost with custom discount and tax: ${total_price_custom}")
