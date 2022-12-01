alien_colors = ["red", "green", "yellow"]
color = "blue"
if color == "green":
    print ("You've earned 5 pts")

if color == "green":
   print("You've just earned 5 pts!")
else:
  print ("You've just earned 10 pts")

color = "yellow"
if color == "green":
    print ("5 pts for you")
elif color == "yellow":
    print ("10 pts for you")
else:
    print ("15 pts for you")

print("\n")
for alien_color in alien_colors:
    if alien_color == "green":
        print("You've just earned 5 pts!")
    else:
        print ("No points for you!")