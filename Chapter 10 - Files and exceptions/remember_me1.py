# saving and reading user-generated data - pt. 1 (pt. 2 - greet_user)

import json

def example_one():
    username = input("Hi, what's your name: ")

    filename = 'username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you when you come back, {username}.")

example_one()

