print ("--- removing all instances of specific values from list ---")

pets = ['cat', 'dog', 'bird', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print (pets)

#let's remove all cats from the list

while 'cat' in pets:
    pets.remove('cat')

print (pets)