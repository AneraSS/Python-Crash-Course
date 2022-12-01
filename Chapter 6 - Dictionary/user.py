print ("--------- looping through all key-value pairs --------")

user = {
    'username': 'arthemis',
    'name': 'anera',
    'surname': 'svarc sosic',
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"\tValue:{value.title()}")

