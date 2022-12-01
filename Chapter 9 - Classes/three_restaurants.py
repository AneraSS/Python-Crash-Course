class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")


# make three instance called from your class.

namaste = Restaurant('Namaste', 'indian')
ilsecondo = Restaurant ('Il secondo', 'italian')
soifusion = Restaurant ('Soi fusion', 'fusion')

print(f"I love {namaste.cuisine_type} food, therefore I love to go to {namaste.name}")
namaste.describe_restaurant()

print(f"I love {ilsecondo.cuisine_type} food, therefore I love to go to {ilsecondo.name}")
ilsecondo.open_restaurant()

print(f"I love {soifusion.cuisine_type} food, therefore I love to go to {soifusion.name}")
soifusion.describe_restaurant()