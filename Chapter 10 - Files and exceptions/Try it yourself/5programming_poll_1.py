# write a "while" loop that asks people why they like programming
# each time someone enters a reason, add their reason to a file that stores all the responses

print ("To stop the loop, enter 'quit'.")
filename = '5programming_pool_1.txt'

while True:
    question = input ("Please, write why you like programming: ")
    if question == 'quit':
        break
    else:
        with open (filename, 'a') as fileobject:
            fileobject.write(f"{question}\n")

