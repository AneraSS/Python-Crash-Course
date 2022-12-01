players = ["martina", "george", "charls", "anita", "quin"]
print(players[0:3]) #or [:3]; works as well as [n:]

print("These are the first three players:")
for player in players[:3]:
    print (player.title())

print("Here are reverse-alphabet first three players:")
for player in sorted(players, reverse=True)[:3]:
    print (player.title())