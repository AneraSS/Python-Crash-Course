favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
take_poll = ['jen', 'edward', 'martin', 'erika']

for name in take_poll:
    if name in favorite_languages.keys():
        print (f"Thanks {name.title()}, but you've already taken the poll.")
    else:
        print (f"Thanks {name.title()}, much appreciated")
