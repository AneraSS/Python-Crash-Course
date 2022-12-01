print ("--- writing to an empty file ---")
# kreiranje iz pythona txt!!

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# here are two argumens in open()
# first: name of file
# second: "w" tells Py to open the file in "write mode"

# w - write mode
# r - read mode
# a - append mode

# CAUTION! If a file with same name already exists, if w used, it will erase the contents
# write () -- to write a string in created txt

print ("--- appending to a file ---")

with open(filename, 'a') as file_object:
    file_object.write("I also love chemistry.\n")
    file_object.write("I love my family so much.")