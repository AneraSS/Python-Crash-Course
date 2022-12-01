# create a .txt file (see pi_digits.txt)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

