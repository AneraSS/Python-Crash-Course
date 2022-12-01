def get_formatted_name (first_name, middle_name, surname):
    """"Return full name neatly formated"""
    full_name = f"{first_name} {middle_name} {surname}"
    return full_name

musician = get_formatted_name('john', 'lee', 'hooker')
print (musician)



