topping_list = []
topping_name = ''

while topping_name != 'quit':
    topping_name = input ("Enter pizza topping ('quit' to stop): ")
    if topping_name != 'quit':
        topping_list.append(topping_name)

print(f"Pizza contains {topping_list}")

while True: #beskonacna petlja
    topping_name = input ("Enter pizza topping ('quit' to stop): ")
    if topping_name != 'quit':
        topping_list.append(topping_name)
    else:
        break

print(f"Pizza contains {topping_list}")