print ("-- letting the user choose when to quit --")

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\n\tEnter 'quit' to end the program."

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
print("done")