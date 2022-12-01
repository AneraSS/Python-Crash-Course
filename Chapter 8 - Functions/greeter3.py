def get_formatted_name(name, surname):
    full_name =f"{name} {surname}"
    return full_name.title()

while True:
    print ("\nPlease tell me your name: ")
    print ("\tEnter 'q' to quit.")
    first_name = input ("First name: ")
    if first_name == 'q':
        break
    last_name = input ("Last name: ")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\tHello, {formatted_name}!")