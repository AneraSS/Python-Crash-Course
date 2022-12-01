# store the "User" class in one module
# store "Privileges" and "Admin" classes in separate module

class User:

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def make_user(self):
        print (f" Summary of user {self.first_name} {self.last_name}")


def show_privileges():
    print("Here is your Admin list of privileges.")