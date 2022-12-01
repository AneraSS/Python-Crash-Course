class User:

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def make_user(self):
        print (f" Summary of user {self.first_name} {self.last_name}")

class Admin(User):
    def __init__(self, first_name, last_name, sex, age, privileges):
        super().__init__(first_name, last_name, sex, age)
        # make a Privilages instance as an attribute in the Admin class
        self.privileges = Privileges(privileges)


# write a separate class privileges
# the class should have one attribute: privileges, that stores a list of strings
class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print (f"Here is your list of privileges: {self.privileges}.")


anera = Admin('anera', 'svarc','female', 31, ["can add post", "can delete post", "can ban user", "etc."])
anera.privileges.show_privileges()