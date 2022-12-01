#pp 43

cars = ["bmw", "audi", "suzuki", "vw", "toyota", "renault"]
cars.sort()
print (cars)
cars.reverse()
print(cars)

# sorted(nn) doesn't affect the actual list vs. .sort() and .reverse()
print ("Here is the original list:", cars)
print ("Here is the sorted list:", sorted(cars))
print ("Here is the original list:", cars)

#length
print ("Number of cars in the list:", len(cars))

