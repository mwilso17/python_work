# Mike Wilson 20 June 2021
# At attempt at representing a car.

class Car:
  """An attempt to represent a car"""

  def __init__(self, make, model, year):
    """Initialize attributes"""
    self.make = make
    self.model = model
    self. year = year

  def get_descriptive_name(self):
    """Returns a neatly formatted descriptive name."""
    descriptive_name = f"{self.year} {self.make} {self.model}"
    return descriptive_name.title()

my_old_car = Car('honda', 'accord', 1995)
print(my_old_car.get_descriptive_name())