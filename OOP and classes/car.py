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
    descriptive_name = f"\n{self.year} {self.make} {self.model}"
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

  def increment_odometer(self, miles):
    """Add given amount to odometer reading"""
    self.odometer_reading += miles

  def fill_gas_tank(self):
    """Prints statement saying that gas has been topped off."""
    print(f"This {self.make.title()} now has a full tank of gas!")


class ElectricCar(Car):
  """Represents aspects of a car, specific to electric cars"""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class"""
    super().__init__(make, model, year)
    self.battery_size = 75

  def describe_battery(self):
    """Prints a statement describing battery size"""
    print(f"This car has a {self.battery_size}-kWh battery.")

  def fill_gas_tank(self):
      """Electric cars don't have a gas tank"""
      print("No need for gas in an electric car!")

my_old_car = Car('honda', 'accord', 1995)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(223_060)
my_old_car.read_odometer()

my_old_car.increment_odometer(321)
my_old_car.read_odometer()
my_old_car.fill_gas_tank()

my_electric_car = ElectricCar('tesla', 'model s', 2018 )
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()
my_electric_car.fill_gas_tank()