print("--------- dictionary of similar objects ---------")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
language = favorite_languages["sarah"].title()
print (f"Sarah's favorite language is {favorite_languages['sarah']}")

print("--------- looping through a dictionary ---------")

for name, language in favorite_languages.items():
    print (f"{name.title()}'s favourite language is {language.title()}")

print("--------- looping through all the keys in the dictionary ---------")

for name in favorite_languages.keys():
    print (name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print (f"Hi, {name.title()}")
    if name in friends:
        print(f"\t{name.title()} loves {language.title()}")
if 'erin' not in favorite_languages.keys():
    print ("Erin, please take the poll!")

print("--------- looping through the dictionary's keys in a particular order ---------")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("--------- looping through all the values in a dictionary ---------")

print ("Following languages were mentioned, alphabethically:")
for language in sorted(favorite_languages.values()):
    print(language.title())

print("----")
#to remove repeats, use set(XX)
for language in set(favorite_languages.values()):
    print(language.title())

print("-------- a list in a dictionary -----------")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")