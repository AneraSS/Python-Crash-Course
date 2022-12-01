# Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message,
# “I know your favorite number! It’s _____.”

import json

number = input("Please, give me your favourite number: ")

filename = 'favourite_number.txt'

with open(filename, 'w') as f:
    json.dump(number, f)