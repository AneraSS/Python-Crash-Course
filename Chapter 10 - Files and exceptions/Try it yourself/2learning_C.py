# .replace() method!
# read in each line from the file you just created (1) and replace Python with C

filename = '1learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C')) # replaces Python with C