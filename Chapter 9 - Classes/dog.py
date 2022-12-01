# let's create a class named dogs
# all dogs have age and name and know these behaviours (sit, roll over)

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """"Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in a response to a command."""
        print(f"{self.name} is now rolling over!")


my_dog = Dog('Riu', 2)
your_dog = Dog ('Laky', 7)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
your_dog.roll_over()