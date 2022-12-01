# start with previous excercise (sending messages)
# call the function send_messages() with a copy of the list of messages
# after calling the function, print both lists to show that the original list  retained its messages


def send_messages(text_messages):
    while text_messages: #loop that walks through messages
        current_messages = text_messages.pop(0) #pop-out that one message, from the beginning
        print(current_messages) #print that one message
        sent_messages.append(current_messages)  #new list that is filled with poped-out messages


received_messages = ['hi', 'how are you?', 'Can I call you later?', 'DND', 'BRB']
sent_messages = []

print ("List of messages:")
send_messages(received_messages[:]) #activate the function, [:] copy of a list

print (f"\nInitial list of messages: {received_messages}")
print (f"New list of messages: {sent_messages}")
