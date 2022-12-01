class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # add an attribute called number_served of default value 0

    def describe_restaurant(self):
        print(f"The {self.name} restaurant serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")

    #because you added self.number_served, you have to make a new method, as well, to make it readable
    def served_number(self):
        # print the number of customers the restaurant has served
        print(f"The restaurant served {self.number_served} times.")

    # add a method called set_number_served() that lets you increment the number of customers who've been served
    def set_number_served(self, number):
        self.number_served += number


# make an instance called restaurant from this class.
restaurant = Restaurant('Namaste', 'indian')
restaurant.describe_restaurant()

# print the number of customers the restaurant has served
restaurant.served_number()

# add a method called set_number_served() that lets you increment the number of customers who've been served
# call this method with any number you like that could represent how many customers were served in a day
restaurant.set_number_served(30)
restaurant.served_number()
restaurant.set_number_served(40)
restaurant.served_number()
restaurant.set_number_served(10)
restaurant.served_number()