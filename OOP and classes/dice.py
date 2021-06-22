# Mike Wilson 22 June 2021
# This program simulates dice rolls and usues classes and methods from the 
# Python standard library

from random import randint

class Die:
  """Represents a die that can be rolled."""

  def __init__(self, sides=6):
    """Initialize the die. 6 by default."""
    self.sides = sides

  def roll_die(self):
    """Return a number between 1 and the number of sides."""
    return randint(1, self.sides)


# Make a 6 sided die and roll it 10 times.
d6 = Die()

results = []
for roll_num in range(10):
  result = d6.roll_die()
  results.append(result)

print("\nThe 10 rolls of a 6 sided dice came up: ")
print(results)


# Make a 10 sided die and roll it 10 times.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
  result = d10.roll_die()
  results.append(result)

print("\nThe 10 rolls of a 10 sided dice came up: ")
print(results)


# Make a 20 sided die and roll it 10 times.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
  result = d20.roll_die()
  results.append(result)

print("\nThe 20 rolls of a 6 sided dice came up: ")
print(results)