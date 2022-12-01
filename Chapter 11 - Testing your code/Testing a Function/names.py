from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me your last name: ")
    if first == 'q':
        break

    formatted_name = get_formatted_name (first, last)
    print(f"\nNeatly formatted name: {formatted_name}")