import yaml

with open('order.yaml') as file:
    py_obj = yaml.safe_load(file)

# 1
invoice_number = py_obj['invoice']
print(f"Invoice number is {invoice_number}\n")

# 2
city = py_obj['bill-to']['address']['city']
lines = py_obj['bill-to']['address']['lines']
state = py_obj['bill-to']['address']['state']
postal = py_obj['bill-to']['address']['postal']
print(f"City: {city}\nLines: {lines}State: {state}\nPostal: {postal}\n")

# 3
product = py_obj['product']
description = []
for el in product:
    description.append(el['description'])
print(f"Description: {', '.join(description)}")
quantity = []
for el in product:
    quantity.append((el['quantity']))
print(f"Quantity: {sum(quantity)}")
total_price = py_obj['total']
print(f"Total price: {total_price}")
