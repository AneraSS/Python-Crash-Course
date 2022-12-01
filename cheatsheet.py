METHODS ON STRINGS
name.title()
name.lower()
name.upper()
name.rstrip() # remove whitespace on the right
name.lstrip() # remove whitespace on the left
name.strip() # remove empty space everywhene

LISTS
print(name[index]) # print list's content from position index
print(name[-1]) # print list's content from last position
name.append(what)
name.insert(where, what)
name.pop() # if empty, then pops from back
name.remove(what)
name.sort() #alphabetical sorting, permanently
sorted(name) #temporary sorting
name.reverse() #reverse-alphabetical sorting, permanently

pp.50
a += 7.5 or a = a + 7.5

FUNCTIONS (pp.147)
def make_pizza (size, *toppings) # when you don't know how much arguments the function accepts (*)
def build_profile(first, last, **user_info) # ** - creates an empty dictionary
#such as this:
def make_car(company, name, **features):
    features['Company'] = company
    features['Name'] = name
    return features
car = make_car('renault', 'megane', color='black', fog_lights=True)
print(car)
RESULTS WITH: {'color': 'black', 'fog_lights': True, 'Company': 'renault', 'Name': 'megane'}


DICTIONARY
#adding stuff to dictionary:
dictionary = {}
dictionary[key] = value # value == variabla

MODULES
see Chapter 8 - Modules

CLASSES
class ElectricCar (Car):
def __init__(self, make, model, year):
    super().__init__(make, model, year)
    # this allows to call a function from a parent class
    #see electric_car.py in Ch9

OPEN FILES

EXCEPTIONS
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You cannot divide with zero!")