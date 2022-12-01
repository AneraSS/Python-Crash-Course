# write a function called send_messages() that prints each text message and moves it to a new list called
# sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages were
# moved correctly.


def send_messages(text_messages):
    while text_messages: #loop that walks through messages
        current_messages = text_messages.pop(0) #pop-out that one message, from the beginning
        print(current_messages) #print that one message
        sent_messages.append(current_messages)  #new list that is filled with poped-out messages


received_messages = ['hi', 'how are you?', 'Can I call you later?', 'DND', 'BRB']
sent_messages = []

print ("List of messages:")
send_messages(received_messages) #activate the function

print (f"\nInitial list of messages: {received_messages}")
print (f"New list of messages: {sent_messages}")
