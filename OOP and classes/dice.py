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