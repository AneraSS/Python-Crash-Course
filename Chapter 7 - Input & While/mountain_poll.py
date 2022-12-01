print ("--- filling a dictionary with user input ---")

responses = {}

# set a flag to indicate the poll is active

polling_active = True

while polling_active:
    #prompt the person's name and response
    name = input ("\nEnter your name: ")
    response = input("\n Which mountain would you like to climb someday? ")
    #store the response in dictionary
    responses[name] = response #dictionary[key]=value dict[key][key1]=value1 (kada je dict u dict)
    #find out will someone else like to take the poll
    repeat = input("Would you like to let another person respond (yes/no): ")
    if repeat == 'no':
        polling_active = False

#polling  is complete, results:
print ("\--- Poll Results ---")
for name, response in responses.items():
    print (f"{name} would like to climb {response}.")



