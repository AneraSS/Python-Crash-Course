print("-------- a list in a dictionary -----------")

#store informaton about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'onions', 'tomato sauce']
}

#summarize the order
print ("EXAMPLE 1a")
print (f"You have ordered the pizza with a {pizza['crust']} crust "
       f"and with the following toppings: {pizza['toppings']}")

#or write it this way: summarize the order
print("EXAMPLE 1b")
print (f"You have ordered the pizza with a {pizza['crust']} crust "
       f"and with the following toppings:")

for topping in pizza['toppings']:
    print (f"\t{topping}")