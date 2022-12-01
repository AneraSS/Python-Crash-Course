print ("--- using the break to exit a loop ---")

prompt = "Please enter a name of a city you've visited: " \
         "\nEnter 'quit' when you've finished. "

while True:
    city = input (prompt)
    if city == 'quit':
        print("Game end.")
        break
    else:
        print (f"I'd like to go to {city.title()}")
