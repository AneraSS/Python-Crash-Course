class User:

    def __init__(self, first_name, last_name, sex, age): # all in brackets are called 'attributes'
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age


    def make_user(self):
        print (f" Summary of user {self.first_name} {self.last_name}")

    def get_prefix(self):
        if self.sex == 'male':
            return 'Mr.' #funkcija vraca string
        else:
            return 'Mrs.'

    def print_prefix(self):
        print (self.get_prefix()) # printa prefiks

    def print_prefixed(self):
        print (f"{self.get_prefix()} {self.last_name}")

