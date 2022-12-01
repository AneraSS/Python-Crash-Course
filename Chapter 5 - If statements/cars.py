cars = ["bmw", "audi", "suzuki", "vw", "toyota", "renault"]
for car in cars:
    if car == "bmw" or car == "vw":
        print(car.upper())
    else:
        print (car.title())