favourite_number = {
    "anera": [7,8],
    "martin": [3, 20],
    "ruth": [5, 13, 45],
    "zina": [11, 22, 46, 98],
    "tea": [25],
}

for name, numbers in favourite_number.items():
    print (f"{name.title()}'s favourite number/s is/are:")
    for number in numbers:
        print(f"\t{number}")