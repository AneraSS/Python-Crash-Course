# REFACTORING
# breaking/moving all into a series functions
    # codes are cleaner and easier to extend

# EXCERCISE 1
import json

def greet_user1():
    """Greet user by name."""
    filename = 'username3.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Hi, what's your name: ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}.")
    else:
        print(f"Welcome back, {username}!")

#greet_user1()

#now, here is refactoring, because greet_user() is doing more than just greeting the user

# EXCERCISE 2

def get_stored_username():
    """Get stored username, if available."""
    filename = 'username3.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("Please, give me your name: ")
    filename = 'username3.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()