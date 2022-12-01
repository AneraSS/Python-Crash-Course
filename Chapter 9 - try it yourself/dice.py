# make a class called "Dice" with one attribute called sides, of default 6
# write a method called roll_die
# that prints a random number (1-6)
# make a 6-sided die and roll it 10x
# previously defined
# makes a random choice between two argument integers (from, to), including both
from random import randint

class Die:
    """Represents a die that can be rolled"""
    def __init__(self, sides=6):
        """Initialize a die."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and 6"""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die() # because it is default sides=6 so it can be empty
results = []
for roll_number in range (0,10):
    result = d6.roll_die()
    results.append(result)
print (f"6-sided die; After 10 rolls, results are: {results}")

# make a 10-sided die, roll  10x
d10 = Die(sides=10)
results = []
for roll_number in range (0,10):
    result = d10.roll_die()
    results.append(result)
print (f"10-sided die; After 10 rolls, results are: {results}")

# make a 20-sided die, roll  10x
d20 = Die(sides=20)
results = []
for roll_number in range (0,10):
    result = d20.roll_die()
    results.append(result)
print (f"20-sided die; After 10 rolls, results are: {results}")