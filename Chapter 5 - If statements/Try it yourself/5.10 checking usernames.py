# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#
# Make a list of five or more usernames called current_users. Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

current_users = ["charlie", "admin", "betty", "cheryl", "sylvia", "bob"]
new_users = ["cynthia", "bob", "donna"]

for new in new_users:
    if new in current_users:
        print (f"Hi, {new.title()}, your name is already taken. Think of a new one!")
    else:
        print (f"Hi, {new.title()}, you're name is unique!")

current_users = ["charlie", "admin", "betty", "cheryl", "sylvia", "bOb"]
new_users = ["cynthia", "BOB", "donna"]

print("\nCase sensitive solution: \n")

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new in new_users:
    if new.lower() in current_users_lower:
        print(f"Hi, {new.title()}, your name is already taken. Think of a new one!")
    else:
        print(f"Hi, {new.title()}, you're name is unique!")

# print("\n")
## nije dovršeno

# for new in new_users:
#     isok = True
#     for current in current_users:
#         if new.lower() == current.lower():
#             print (f"Change your name, {new.title()}")
#         else:
#             print (f"OK, you're good to go, {new.title()}")