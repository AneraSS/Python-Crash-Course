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


class Admin(User):
    # administrator is a special kind of user
    # Admin inherits from User class
    # add an attribute "privileges" that stores a list of strings
    # like: "can add post", "can delete post", "can ban user", etc.
    def __init__(self, first_name, last_name, sex, age, privileges):
        super().__init__(first_name, last_name, sex, age) # this is all that's present in class User
        self.privileges = privileges

    # write a method called show_privileges() that lists the administrator set of privileges
    def show_privileges(self):
        print (f"Here is your list of privileges: {self.privileges}.")

# create an instance of Admin and call method
anera = Admin('anera', 'svarc','female', 31, ["can add post", "can delete post", "can ban user", "etc."])
anera.show_privileges()