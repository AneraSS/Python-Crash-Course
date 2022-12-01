print ("--- using continue in a loop --- ")

# using continue to return to the beginning  of the loop based on the result of a conditional test
#eg. loop counts from 1 to 10 but prints out even numbers

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

