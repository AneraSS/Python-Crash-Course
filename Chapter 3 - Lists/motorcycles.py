motorcycles = ["honda", "yamaha", "suzuki", "bmw"]
print (motorcycles)
motorcycles[0] = "ducati" #exchange
print (motorcycles)
motorcycles.append("mercedes") #add
print(motorcycles)

cars = []
cars.append("bmw")
cars.append("renault")
cars.append("fiat")
cars.append("skoda")
print(cars)
cars.insert(1, "mercedes") #insert at certain position
print(cars)

print (motorcycles)
del motorcycles[3] #delete at certain position
print (motorcycles)

print(cars)
never_owned = f"I have never owend a {cars[0].upper()} and {cars[1].title()}"
print (never_owned)
popped_cars = []
popped_cars.append(cars.pop(0))
popped_cars.append(cars.pop(0))
print (popped_cars)
print (cars)

print (motorcycles)
motorcycles.remove("suzuki")
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (f"{too_expensive} is too expensive for me.")
print (motorcycles)

