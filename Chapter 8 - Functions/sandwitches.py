# write a function that accepts a list of items a person wants in a sandwich
# function has one parameter that collects as many items as the call provides
# print a summary of the sandwich being ordered
# call function nx using different number of arguments


def sandwitch (*toppings):
    print (toppings)


sandwitch('salad')
sandwitch('tomato', 'cheese', 'salad')