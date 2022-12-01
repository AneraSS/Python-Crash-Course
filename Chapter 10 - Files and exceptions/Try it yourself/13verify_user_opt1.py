import json

def get_stored_username():
    """Get stored username, if available."""
    try:
        with open('database.json') as f:
            username = json.load(f)
    except FileNotFoundError:
        return print("File not found...") # or None
    else:
        return username # a ne : print(f"Hello, {username}")

def greet_user():
    """Greet username by name."""
    username = get_stored_username()
    if username:
        answer = input(f"Is your name {username}? Y/N ")
        if answer == 'y':
            print(f"Hi, {username}")
        else:
            new_name = input("Please, give me your name: ")
            with open('database.json', 'w') as f:
                json.dump(new_name,f)
                print(f"I'll add you to the database, {new_name}")

greet_user()

# NE ZNAM RASCLANITI NA DIJELOVE