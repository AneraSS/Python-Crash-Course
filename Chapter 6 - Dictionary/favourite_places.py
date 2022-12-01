favorite_places={
    'martin': ['iceland', 'japan'],
    'ruth': ['korea', 'indonesia'],
    'anera': ['singapore', 'switzerland'],
}

for name, places in favorite_places.items():
    print (f"{name.title()} loves: {places}")

print ("-----")

for name, places in favorite_places.items():
    print (f"{name.title()} loves:")
    for place in places:
        print (f"\t{place.title()}")