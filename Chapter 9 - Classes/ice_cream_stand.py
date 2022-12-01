# ice cream stand is a specific kind of restaurant
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")

# write a class called IceCreamStand that inherits from the Restaurant class
class IceCreamStand(Restaurant):
    # add an attribute called flavors
    # write a method that displays these flavours
    def __init__(self, name, cuisine_type, *flavours): # child constructor
        super().__init__(name, cuisine_type) # mother constructor
        self.flavours = flavours

    def display_flavour(self):
        print(f"We have these flavours: {self.flavours}")

my_cream = IceCreamStand ('Amelie', 'ice cream', 'straciatella', 'chocolate', 'vanilla')
#print (f"I love {my_cream.name}, because it's an {my_cream.cuisine_type} restaurant selling {my_cream.flavours}")
my_cream.display_flavour()

