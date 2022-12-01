person_0 = {
    "name": "martin",
    "surname": "sosic",
    "age":32,
    "place": "zagreb",
}
person_1 = {
    "name": "anera",
    "surname": "svarc sosic",
    "age":32,
    "place": "zurich",
}
person_2 = {
    "name": "ruth",
    "surname": "svarc ",
    "age":26,
    "place": "koeln",
}
# store all three people in a list named people
peoples = [person_0, person_1, person_2]

#loop throuh your list and print everything you know abour a person
for people in peoples:
    print (people)

print ("------")

#loop but nicely
peoples = {
    'person_0': person_0,
    'person_1': person_1,
    'person_2': person_2,
}

for key, value in peoples.items():
    print (f"{key} contains: {value}")

print ("------")

# or even more nicely, but not as asked:

for key, value in person_0.items():
    print(f"{key} : {value}")
print("\n")

for key, value in person_1.items():
    print(f"{key} : {value}")

print("\n")
for key, value in person_2.items():
    print(f"{key} : {value}")