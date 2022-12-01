age = 16
if age <= 4:
    print ("Admission is free.")
elif age <= 18:
    print("Admission is $25.")
elif age >65:
    print("Admission is free.")
else:
    print ("Admission is $40.")

age = 72
if age <= 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 0
print (f"You have to pay ${price} for the admission.")