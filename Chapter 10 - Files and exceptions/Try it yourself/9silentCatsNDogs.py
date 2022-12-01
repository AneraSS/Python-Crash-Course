# Modify your except block in Exercise 10-8 to fail silently if either file is missing.

def readNprintSilently():
    try:
        with open('cats.txt', encoding='utf-8') as f:
            contents = f.read()
            print(f"In cats.txt are following names: \n{contents}")
    except FileNotFoundError:
        pass

    try:
        with open('dogs.txt', encoding='utf-8') as f:
            contents = f.read()
            print(f"\nIn dogs.txt are following names:\n{contents}")
    except FileNotFoundError:
        pass
    
readNprintSilently()