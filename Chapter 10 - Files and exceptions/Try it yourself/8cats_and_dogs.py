# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names
# of dogs in the second file. Write a program that tries to read these files and print the contents of the
# file to the screen. Wrap your code ina try-except block to catch the FileNotFound error, and print a
# friendly message if a file is missing. Move one of the files to a different location on your system, and make
# sure the code in the except block executes properly.

def readNprint():
    try:
        with open('cats.txt', encoding='utf-8') as f:
            contents = f.read()
            print(f"In cats.txt are following names: \n{contents}")
    except FileNotFoundError:
        print("I'm printing a friendly message that the file is missing.")

    try:
        with open('dogs.txt', encoding='utf-8') as f:
            contents = f.read()
            print(f"\nIn dogs.txt are following names:\n{contents}")
    except FileNotFoundError:
        print("I'm printing a friendly message that the file is missing.")

readNprint()
