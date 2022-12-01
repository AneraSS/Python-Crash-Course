poll_active = True
results = {}

while poll_active:
    name = input ("Your name: ")
    location = input ("Dream location for vacation: ")
    results[name]=location
    question = input("Would someone else like to add their dream location (yes/no): ")
    if question == 'no':
        poll_active = False

print ("\nHere are the results of the poll: \n")

for name, location in results.items():
    print (f"{name}'s dream vacation would be in {location}.")
