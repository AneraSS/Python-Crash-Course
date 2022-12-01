# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.
from random import choice

select = 4
possibilities = [1,2,4,6,78,99,65,122,34,67, 'a', 'n', 'e', 'r', 's']


def get_winning_ticket(possibilities):
    winning_ticket = []
    for i in range(0, select+1):
        pulled_char = choice(possibilities)
        if pulled_char not in winning_ticket:  # so it doesn't get pulled twice!
            winning_ticket.append(pulled_char)
    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    # winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    ticket = []
    for i in range(0, select+1):
        pulled_char = choice(possibilities)
        if pulled_char not in ticket:  # so it doesn't get pulled twice!
            ticket.append(pulled_char)
    return ticket


winning_ticket = get_winning_ticket(possibilities) # zasto?
won = False
plays = 0
max_tries=10_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays +=1
    if plays >= max_tries:
        break

if won:
    print (f"Winning ticket is: {winning_ticket}")
    print (f"Your ticket is: {new_ticket}")
    print (f"You had to play {plays} times to win!")

else:
    print(f"You haven't won, although we played {plays} times.")
    print (f"The winning ticket was: {winning_ticket}")


MARTIN
KAKO SI TU PRIČU U GLAVI SLOŽITI