# Add an if test to hello_admin.py to make sure the list of users is not empty.
#
# If the list is emtpy, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

users = ["charlie", "admin", "betty", "cheryl", "sylvia", "bob"]
#users = []

if users:
    for user in users:
        print (f"Hi there, {user.title()}!")
else:
    print ("Hey - there are no users!")

