# Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
#
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

ordinal_numbers = []
for number in range (1,10):
    ordinal_numbers.append(number)
print(ordinal_numbers)

#ili:
#ordinal_numbers = list(range(1,10))

# add st, nd, rd, th to each using if-elif-else

for number in ordinal_numbers:
    if number == 1:
        print (f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print (f"{number}th")

#alternativa:
print ("----------------")
for number in ordinal_numbers:
    suffix = None
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{number}{suffix}")
