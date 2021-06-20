# Mike Wilson 20 June 2021
# At attempt at representing a car.

class Car:
  """An attempt to represent a car"""

  def __init__(self, make, model, year):
    """Initialize attributes"""
    self.make = make
    self.model = model
    self. year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """Returns a neatly formatted descriptive name."""
    descriptive_name = f"{self.year} {self.make} {self.model}"
    return descriptive_name.title()

  def read_odometer(self):
    """Print a statement showing the car's mileage"""
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    """
    Set odometer to a given value.
    Reject change if odometer would roll back?
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer")

my_old_car = Car('honda', 'accord', 1995)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(223_060)
my_old_car.read_odometer()