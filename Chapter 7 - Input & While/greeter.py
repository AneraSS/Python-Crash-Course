print ("-- writing clear prompts --")

name = input ("Please enter your name: ")
print (f"Hello, {name}!")

prompt = "If you tell us who you are, we can personalize that message. " \
         "What is your first name? "

#opcija 2 za ovaj 2. red:
# prompt += "\nWat is your first name?

name = input (prompt)
print (f"Hello, {name}!")