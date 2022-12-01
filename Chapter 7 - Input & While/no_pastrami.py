sandwich_orders = ['ham', 'pastrami', 'tuna', 'pastrami', 'avocado', 'chicken', 'pastrami', 'egg', 'pastrami', 'vege']
finished_sandwiches = []

print ("Sadly, we are out of pastrami sanwich.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:  # loop through the list
    current_sandwich = sandwich_orders.pop(0) # s pozicije (0), ako je (), onda ide odozada
    print (f"I made you a {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print (f"\nOld list: {sandwich_orders}")
print (f"New list: {finished_sandwiches}")