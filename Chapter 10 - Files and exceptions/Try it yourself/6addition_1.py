# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
# Add them together and print the result. Catch the TypeError if either input value is not a number,
# and print a friendly error message. Test your program by entering two numbers and then by entering some text
# instead of a number.

def addition():
    print("To quit enter 'q'.")

    while True:
        try:
            one = input("Please enter firs number: ")
            if one == 'q':
                break
            else:
                x = int(one)
            two = input("Please enter the second number: ")
            if two == 'q':
                break
            else:
                y = int(two)
            sum = x + y
            print(f"Resulting: {x}+{y}={sum}")
        except:
            print("Either input value is not a number. This is a friendly error message.")

addition()




