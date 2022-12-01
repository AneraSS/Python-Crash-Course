# Write a while loop that asks people why they like programming. Each time someone enters a reason,
# add their reason to a file that stores all the responses.

# WEB ANSWER

filename = '5programming_poll_2.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")