# saving and reading user-generated data - pt. 2 (pt. 1 - remember_me)

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
