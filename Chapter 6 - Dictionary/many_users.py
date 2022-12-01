print ("---- a dictionary in dictionary ----")
users ={
    'eaeinstein': {
        'name': 'albert',
        'surname': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'name': 'marie',
        'surname': 'curie',
        'location': 'paris',
    },
}

for nickname, user_name in users.items():
    print(f"Username: {nickname}")
    full_name = f"{user_name['name']} {user_name['surname']}"
    location = user_name['location']
    print (f"\tFull name: {full_name.title()}")
    print (f"\tLocation: {location.title()}")