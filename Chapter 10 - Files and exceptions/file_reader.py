file_name = 'pi_digits.txt'


print("\n1 ---reading an entire file---")
# printed out just as it is in .txt
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print (contents.rstrip()) #rstrip if empty space on the right is present in .txt

print("\n2 ---reading line by line---")
# each line separately printed out (just like in .txt) but with empty line before each printed line
with open(file_name) as file_object:
    for line in file_object:
        print (line)

print("\n--if .rstrip() added:--")
#add .rstrip() to remove empty space after each line
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n3 ---making a list of lines from a file---")
with open(file_name) as file_object:
    lines = file_object # takes each line from the file and stores it in a list
for line in lines:      # use for loop to print each line from 'lines'
    print (line.rstrip())

print("\n4 ---working with a file's contents---")
with open(file_name) as file_object:
    lines = file_object.readline()

pi_string = ''
for line in line:
    pi_string += line.rstrip()
            # .rstrip() will have empty space between sections in same line => lenght 1
            # .strip() removes all empty space present in pi_string => affects lenghth, length 1 != length 2

print(pi_string) # print certain part [:52] -> first 52 digits
print(len(pi_string))
