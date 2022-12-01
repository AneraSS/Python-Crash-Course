
person_age = input ("How old are you? ")
person_age = int(person_age)

if person_age < 3:
    print ("The ticket is free")
elif person_age < 12:
    print("The ticket is $10.")
else:
    print("The ticket is $15.")

