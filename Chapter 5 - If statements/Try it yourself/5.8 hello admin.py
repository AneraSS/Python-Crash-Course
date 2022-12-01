# Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they
# log in to a website. Loop through the list, and print a greeting to each user:
# - If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# - Otherwise, print a generic greeting, such as Hello Eric, thank you for loggin in again.

users = ["charlie", "admin", "betty", "cheryl", "sylvia", "bob"]

for user in users:
    if user == "admin":
        print (f"Hi, {user.upper()}, would you like your stat report?")
    else:
        print (f"Hi, {user.title()}!")