class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")


# make an instance called restaurant from your class.
# print the two attributes individually and call both methods.

restaurant = Restaurant('Namaste', 'indian')

print(f"I love {restaurant.cuisine_type} food, therefore I love to go to {restaurant.name}")
restaurant.describe_restaurant()
restaurant.open_restaurant()