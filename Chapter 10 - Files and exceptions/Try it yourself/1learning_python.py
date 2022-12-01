# write a program that reads the file
# and prints it three times
# print the contents once by reading it in the entire file
# once by looping over the file object
# and once by storing the lines in a list and then working with them outside the 'with' block

def repeat_by_looping(filename):
    with open(filename) as file_object:
        contents = file_object.read()
    for repeat in range(1,4):
        print(f"{repeat}. time: ")
        print(contents)

# repeat_by_looping('1learning_python.txt')


# print the contents once by reading it in the entire file
def reading_entire_file (filename):
    print("1) Print the contents once by reading it in the entire file: ")
    with open (filename) as file_object:
        contents = file_object.read()
    print(contents)

reading_entire_file('1learning_python.txt')

# once by looping over the file object
def by_looping (filename):
    print("2) Print the contents once by looping over the file object: ")
    with open (filename) as file_object:
        for line in file_object:
            print(line.strip()) # strip to remove empty lines in-between

by_looping('1learning_python.txt')

# and once by storing the lines in a list and then working with them outside the 'with' block
def by_storing_in_list(filename):
    print("3) Print the contents once by storing the lines in a list "
          "and then working with them outside the 'with' block: ")
    with open(filename) as file_object:
        lines = ''
        lines = file_object.readlines()

    for line in lines:
        print (line.strip())

by_storing_in_list('1learning_python.txt')