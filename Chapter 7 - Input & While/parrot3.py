print ("-- using a flag --")
# flag can be called any name we want and will be active as long as its statement is TRUE

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\n\tEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print ("Quit? OK! Done.")
    else:
        print(message)

#so, the program starts with an active state
#as long as active (True), the loop will run