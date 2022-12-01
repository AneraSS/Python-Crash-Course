# Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and
# add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the
# file.

filename = '4guest_book.txt'

print ("If you want to exit, write 'quit'.")

while True:
    name = input ("Please, state your name: ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
        print (f"Hi {name}, your name was added to the guest book.")