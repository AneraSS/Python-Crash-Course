class User:

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        # add an attribute called login_attempt
        self.login_attempt = 0

    # write a method called increment_login_attempts() that increments the value of loin_attempts by 1
    def increment_login_attempts(self):
        self.login_attempt += 1

    # write another method called reset_login_attempts() that resets the value of login_attempts() to 0
    def reset_login_attempts(self):
        self.login_attempt = 0

    def make_user(self):
        print (f" Summary of user {self.first_name} {self.last_name}")


# make an instance of the User class
myself = User('anera', 'svarc', 'female', 32)
myself.make_user()

# call increment_login_attempt() several times
myself.increment_login_attempts()
myself.increment_login_attempts()
myself.increment_login_attempts()
myself.increment_login_attempts()

# print value of login_attempts to make sure it was incremented properly
print (f" You have logged in {myself.login_attempt} times.")

myself.increment_login_attempts()
myself.increment_login_attempts()
print (f" You have logged in {myself.login_attempt} times.")

# call reset_login_attempts()
# print login_attempts again to make sure it was reset ot 0
myself.reset_login_attempts()
print (f" You have logged in {myself.login_attempt} times.")