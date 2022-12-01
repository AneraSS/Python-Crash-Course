#dictionaries
alien_0 = {"color": "green", "points": "5"}
print(alien_0["color"])
print(alien_0["points"])

print ("-------------")

new_points = alien_0["points"]
print (f"You got {new_points} pts!")

print ("---- adding new key-value pairs ---------")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print (alien_0)

print ("----- starting with an empty dictionary --------")

alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

print ("----- modifying values in a dictionary --------")

alien_0 = {"color": "green"}
print (f"Alien is color {alien_0['color']}")
alien_0 = {"color": "yellow"}
print(f"Alien is color {alien_0['color']}")

print("---------------- change alien position ----------")
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print (f"Original position of alien is: {alien_0['x_position']}")
#move the alien to the right
#determine how far will he move based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"]== "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] =alien_0["x_position"] + x_increment
print(f"New alien position: {alien_0['x_position']}")

print("---------------- remove key-value pairs ----------")

alien_0 = {"color": "green", "points": "5"}
print(alien_0)

del alien_0["points"]
print (alien_0)

print("---------------- a list of dictionaries ----------")
print ("EXAMPLE 1a")
alien_0 = {"color": "green", "points": "5"}
alien_1 = {"color": "yellow", "points": "10"}
alien_2 = {"color": "red", "points": "15"}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print (f"{alien}")

print("\n")
print ("EXAMPLE 1b")

aliens = {
    "alien_0": alien_0,
    "alien_1": alien_1,
    "alien_2": alien_2}

for alien, values in aliens.items():
    print(f"{alien} contains {values}")

print ("\nEXAMPLE 2")

#make an empty list to store aliens
aliens = []

#make 30 green aliens
for alien_number in range (0,30):
    new_alien = {"color": "green", "points": "5", "speed":"slow"}
    aliens.append(new_alien)

#show the first three aliens
for alien in aliens[:5]:
    print(alien)
print ("etc.")

#show how many aliens were created
print (f"\tTotal numbers of alien being created: {len(aliens)}")

print ("\nEXAMPLE 3")
#lets make first three aliens yellow, remaining 27 should stay green

aliens = []
#creating all green
for alien_number in range(30): #or range (0,30)
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

#changing first three to yellow, 10, medium
for alien in aliens[0:3]:
    if alien['color'] == "green":
        alien['color'] = "yellow"
        alien['points'] = 10
        alien['speed'] = "medium"

#now print first 5 aliens to see the change
for alien in aliens[:5]:
    print(alien)
print ("...")

#and now change yellow to red using elif
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print ("...")
