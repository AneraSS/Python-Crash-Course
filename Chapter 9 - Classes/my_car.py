# now we well make a separate file called my_car.py (vs. car.py)
# this file will impot the Car class and then create an instance from the class.

from car4 import Car

my_new_car = Car ('audi', 'a4', 2019)
print (my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()