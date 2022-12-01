# pp. 179 (car6 + elcar4)


from car6 import Car
from electric_car4 import ElectricCar as EC # alias is "EC"

my_beetle = Car('volkswagen', 'beetle', 2019)
print (my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2019)
print (my_tesla.get_descriptive_name())
