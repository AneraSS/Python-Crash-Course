# [] indicates a list
# individuals separated by ,

# list that contains few types of bicycles

bicycles = ["trek", "cannondale", "redline", "specialized", "mountain", "city"]
print (bicycles)

#to accesss a specific element in the list
# index position starts with 0
print (bicycles[0])
print(bicycles[3])
print (bicycles[2].title())
print (bicycles[-2].title())

message1 = f"My first bike was a {bicycles[0].title()}."
print (message1)

message2 = f"I have never heard of a {bicycles[1].title()}."
print (message2)