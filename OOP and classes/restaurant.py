# Mike Wilson 20 June 2021
# This program creates a class that models a restuarant. 

class Restaurant:
  """a model of a restaurant"""

  def __init___(self, name, cuisine):
    """initialize name and cuisine attributes"""
    self.name = name
    self.cuisine = cuisine

  def describe_restaurant(self):
    """describes the restaurant"""
    print(f"{self.name} is a {self.cuisine} restaurant.")

  def open_restaurant(self):
    """opens the restaurant for business"""
    print(f"{self.name} is now open for business!")

pizza_palace = Restaurant('Pizza Palace', 'pizza')
print(f"{pizza_palace.name}, {pizza_palace.cuisine}")
pizza_palace.describe_restaurant()
pizza_palace.open_restaurant()