# Mike Wilson 20 June 2021
# This program attempts to make a model of a dog.

class Dog:
  """a simple attempt to model a dog"""

  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simulates dog sitting down"""
    print(f"{self.name} is now sitting")

  def roll_over(self):
    """Simulate rolling over"""
    print(f"{self.name} rolled over!")