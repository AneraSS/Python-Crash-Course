dogs = ["whippet", "border coli", "german shepard", "french bulldog", "mastif", "puddle"]
print ("first three animals in the list are:")
for dog in dogs[:3]:
    print(dog)

for i in range(0, len(dogs)):
    print("At number", i, "is dog:", dogs[i])

print ("Three dogs from the middle of the list:")
for dog in dogs[2:5]:
    print(dog)
print ("Last three are:")
for dog in dogs[3:]:
    print(dog)

