sandwich_orders = ['ham', 'tuna', 'avocado', 'chicken', 'egg', 'vege']
finished_sandwiches = []

while sandwich_orders:  # loop through the list
    current_sandwich = sandwich_orders.pop()
    print (f"I made you a {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print (f"\nOld list: {sandwich_orders}")
print (f"New list: {finished_sandwiches}")