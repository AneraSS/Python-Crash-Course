#3-1 & 3-2
friends = ["zina", "tanja", "Tea", "Matea", "Ruth", "Gloria", "Matija", "Ana", "Anita"]

message1 = f"My first friend, from my primary school, was {friends[0].title()}."
print (message1)

message2 = f"Three of my best friends form my secondary school were: {friends[1].title()}, {friends[2]}, and {friends[3]}."
print (message2)

message3 = f"My sister's name is {friends[-5]}."
print (message3)

message4 = f"My new family members are {friends[-4]} and {friends[-3]}."
print(message4)

message5 = f"One of my newest friends are {friends[-2]} and {friends[-1]}."
print (message5)

#3-3
transportation = ["tram", "car", "bike", "scooter", "romobil"]
message6 = f"I never travel by {transportation[0]} any more. " \
           f"\nI always use a {transportation[1]}. " \
           f"\n\tAlthough I used to use a {transportation[2]} during my university days. " \
           f"\tI have never possesed a {transportation[-2]}, while a {transportation[-1]} I had had."
print(message6)

#3-4, 3-5
invites = ["Martin", "ruth", "Einstein", "Camus"]
print (f"{invites[0]}, please come to my dinner party")
print (f"{invites[1].title()}, please come to my dinner party, as well!")
print (f"Mr. {invites[-2]}, would you like to come from your grave to my party?")
print (f"Would Mr. {invites[-1]} feel any pleasure to come to my dinner party?")
print (f"{invites[-1]} can't make it to the dinner party.")
invites.remove("Camus")
invites.append("Riu")
print (invites)
print (f"{invites[0]}, please come to my dinner party")
print (f"{invites[1].title()}, please come to my dinner party, as well!")
print (f"Mr. {invites[-2]}, would you like to come from your grave to my party?")
print (f"Would Mr. {invites[-1]} feel any pleasure to come to my dinner party?")

#3-6
invites.insert(0, "Beyonce")
invites.insert(2, "Shakira")
invites.append("JLo")
print(invites)

#3-7
print ("only two people can come to the dinner party!")
print (f"{invites.pop(0)}, {invites.pop(0)}, {invites.pop(0)}, {invites.pop(0).title()} and {invites.pop(0)} cannot come to the party!")
print (f"only {invites[0]} and {invites[1]} can come to my uber cool party.")
del invites [0] #brisanje ljudi s popisa
del invites [0]
print (invites)

#3-8
places = ["Thailand", "Japan", "Borneo", "New Zeland", "The USA", "Tanzania"]
print ("Places I'd like to visit:", places)
print ("Places in the alphabetical order", sorted(places))
print ("See, the list is still in the original order:", places)
print ("Places in the reverse order, temporarily:", sorted(places, reverse=True))
print ("Still original:", places)
places.reverse()
print ("Now, let's permamanently change the order in reverse:", places)
places.sort()
print ("OK, here is in the alphabethical order, permanently:", places)

#3-9
print ("Number of people I will invite to the party:", len(invites))
print ("Nuber of places I'd like to visit:", len(places))

#3-10
colors = ["green", "blue", "red", "pink", "orange", "brown", "black", "white"]
print ("Colors alphabetical, temp.:", sorted(colors))
print ("Colors reverse, temp.:", sorted (colors, reverse=True))
print ("See, as original:", colors)
colors.sort()
print ("Colors alphabetical, perm.:", colors)
colors.reverse()
print ("Colors reverse, perm.:", colors)
print ("Number of mentioned colors:", len(colors))