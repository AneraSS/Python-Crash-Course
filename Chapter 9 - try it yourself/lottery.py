# make a list or tuple containing a series of 10 numbers and 5 letters
# randomly select 4 numbers or letters from the list
# and print a message saying that any ticket matching these 4 numbers/letters wins a prize

from random import choice

possibilities = [1,2,4,6,78,99,65,122,34,67, 'a', 'n', 'e', 'r', 's']
select = 4

new_list = []
for i in range (0,select):
    pulled_char = ''
    pulled_char = choice(possibilities)
    if pulled_char not in new_list: # so it doesn't get pulled twice!
        new_list.append(pulled_char)
        print(f"We pulled {pulled_char}!")
print (new_list)