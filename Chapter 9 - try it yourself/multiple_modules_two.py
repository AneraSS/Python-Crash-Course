# store the "User" class in one module
# store "Privileges" and "Admin" classes in separate module

from multiple_modules_one import User

class Admin(User):
    def __init__(self, first_name, last_name, sex, age, privileges):
        super().__init__(first_name, last_name, sex, age) # this is all that's present in class User
        self.privileges = privileges

    def show_privileges(self):
        print (f"Here is your list of privileges: {self.privileges}.")
