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


my_dog = Dog('Spark', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Rover', 2)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()