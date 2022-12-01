def describe_pet(pet_name, pet_type='whippet'): #defaultne vrijednosti moraju biti na kraju
    """"Display info about pets"""
    print (f"\nI have a {pet_type}")
    print (f"\tMy {pet_type} is called {pet_name}")

describe_pet('Riu')
describe_pet(pet_name='Riu')
describe_pet(pet_name='Kira', pet_type='cat')
