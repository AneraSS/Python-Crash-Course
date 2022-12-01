print ("--- moving items from one list to another ---")

# start with users that need to be verified,
# and an empty list  to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'june']
confirmed_users = []

# verify each user until there are no unverified users
# move verified user to the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print (f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# display all confirmed users:
print ("\nFollowing users were confirmed: ")
for confirmed_user in confirmed_users:
    print (f"{confirmed_user.title()}")