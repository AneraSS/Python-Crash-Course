print ("--- the modulo operator ---")

# tells you the value after decimal dot (remainder)
# eg. 5%3 = 2, 6%3 = 0, 7%3=1

number = input ("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("Number is even.")
else:
    print ("Number is odd.")