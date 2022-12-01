def build_person(name, surname, age = None):
    """Return a dictionay of information about people"""
    person = {'first:': name, 'last:': surname}
    if age:
        person['age']= age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print (musician)