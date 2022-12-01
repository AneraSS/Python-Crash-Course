def describe_pet(pet_type, pet_name):
    """Display info about pets"""
    print (f"\nI have a {pet_type}")
    print (f"\tMy {pet_type} is called {pet_name}")

describe_pet('whippet', 'Riu')
describe_pet('cat', 'Kira')
describe_pet(pet_type='pointer', pet_name='Laky')
describe_pet(pet_name='Capi', pet_type='cat')