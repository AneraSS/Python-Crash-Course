requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print ("Hold the anchovies!")

answer = 17
if answer !=42:
    print ("\nThat's not the correct answer, please try again")

requested_topping = ["mushroom", "onion", "pineapple"]
if "mushroom" in requested_topping:
    print("\nAdding mushrooms")
if "onion" in requested_topping:
    print ("Adding onions")
if "tomato sauce" in requested_topping:
    print ("Adding tomato sauce")
print("Pizza is now done!")

print ("\n")

requested_topping = []
if requested_topping:
    for topping in requested_topping:
        print (f"Adding teh {topping}")
    print ("The pizza is now done")
else:
    print ("You sure you want a plain pizza?")

print("\n")
#multiple lists
available_toppings = ["mushroom", "onion", "pineapple", "pepperoni", "mozarella", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese", "onion"]

for requested in requested_toppings:
    if requested in available_toppings:
        print (f"We've added {requested}")
    else:
        print (f"Sorry, no {requested} available")
print ("You happy with your pizza?")
