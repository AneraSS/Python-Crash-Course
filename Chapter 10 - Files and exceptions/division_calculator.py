# EXCEPTIONS

# handling the ZeroDivisionError
# if divided by 0: Python >> ZeroDivisionError: division by zero

# using try-except Blocks
def first_task():
    try:
        print (5/0)
    except ZeroDivisionError:
        print("You cannot divide with zero!")

#first_task()

# using exceptions to prevent crashes
def second_task():
    print("Give me two numbers and I'll divide them.")
    print("Enter 'q' to quit.")

    while True:
        first_number = input("\nEnter first number: ")
        if first_number == 'q':
            break
        second_number = input("\nEnter second number: ")
        if second_number == 'q':
            break
        answer = int(first_number)/int(second_number)
        print(answer)

#second_task()
# if divided with 0, Python answers>> ZeroDivisionError: division by zero

# the else block
# prevent Python from crashing
def third_task():
    print("Give me two numbers and I'll divide them.")
    print("Enter 'q' to quit.")

    while True:
        first_number = input("\nEnter first number: ")
        if first_number == 'q':
            break
        second_number = input("\nEnter second number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number)/int(second_number)
        except ZeroDivisionError:
            print ("You cannot divide with zero!")
        else:
            print(answer)

third_task()
# now Python will tell you instead of crashing on you.

