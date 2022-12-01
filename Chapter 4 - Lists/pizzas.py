pizzas = ["margarita", "mix", "vegetarian", "pepperoni"]
for pizza in pizzas:
    print (f"I love {pizza} pizza")
print ("we have to order more pizza!")

Ruths_pizzas = pizzas[:]
Ruths_pizzas.append("quattro")
print(Ruths_pizzas)

print("My pizzas are:")
for pizza in pizzas:
    print(pizza)

print("Ruth's pizzas are:")
for pizza in Ruths_pizzas:
    print(pizza)