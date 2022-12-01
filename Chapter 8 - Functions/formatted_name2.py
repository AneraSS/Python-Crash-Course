def get_formatted_name (first_name, surname, middle_name=''):
    """"Return full name neatly formated"""
    if middle_name: #ili: if middle_name != '':
        full_name = f"{first_name} {middle_name} {surname}"
    else:
        full_name = f"{first_name} {middle_name} {surname}"
    return full_name.title()

musician = get_formatted_name('john','hooker', 'lee')
print (musician)



