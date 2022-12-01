# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

your_name = input ("Please, tell me your name and I'll create a .txt with your name: ")

with open (your_name, 'w') as file_object:
    file_object.write(your_name)