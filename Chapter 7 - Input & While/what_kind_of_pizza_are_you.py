#unesi topinge
# koja je to pizza na temelju tih toppinga
# ako je nema, napravi novu pizzu

#baza topinga
topping_base = ['onions', 'paprika', 'mushrooms', 'tomato', 'pepperoni', 'ham', 'cheese', 'cream', 'corn']
print (f"These are our pre-defined toppings, but we can get additional ones, as well: \n{topping_base}.")

pizzas = {
    'cheese' : ['cheese', 'tomato'],
    'pepperoni_pizza' : ['tomato', 'cheese', 'pepperoni'],
    'slavonia' : ['tomato', 'cheese', 'cream', 'pepperoni', 'corn', 'onions'],
    'vegetable' : ['tomato', 'cheese', 'mushrooms', 'onions', 'corn', 'paprika'],
    'capricciosa' : ['tomato', 'cheese', 'mushrooms', 'ham'],
}

user_toppings = []
topping_name = ''

#skupljanje toppinga
while topping_name != 'quit':
    topping_name = input("\nWhat topping would you like (to stop, enter 'quit'): ")
    if topping_name != 'quit':
        user_toppings.append(topping_name)

print (f"\nYou entered following pizza toppings: {user_toppings}")

#pretraga postoji li pizza s takvim toppinzima

pizza_exists = False
for name, toppings in pizzas.items():
    if sorted(user_toppings) == sorted(toppings):
        pizza_exists = True
        print (f"\nYour just ordered a {name}. Bon appetit!")

# ukoliko ne postoji takva pizza:

if pizza_exists == False:           # ili if not pizza_exists:
    new_pizza_name = input ("\nWe don't have such pizza. \nGive us a name and we will add it to our offer: ")
    pizzas[new_pizza_name] = user_toppings
    print (f"Congrats! '{new_pizza_name}' was added to our menu: "
           f"\n\tOur menu: {pizzas}")




