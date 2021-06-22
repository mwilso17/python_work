# Mike Wilson 20 June 2021
# This program creates a class that models a restuarant. 

class Restaurant:
  """a model of a restaurant"""

  def __init__(self, name, cuisine):
    """initialize name and cuisine attributes"""
    self.name = name
    self.cuisine = cuisine
    self.customers_served = 0

  def describe_restaurant(self):
    """describes the restaurant"""
    print(f"\n{self.name.title()} is a {self.cuisine} restaurant.")

  def open_restaurant(self):
    """opens the restaurant for business"""
    print(f"{self.name.title()} is now open for business!")

  def set_number_served(self, customers):
    """Sets the number the restaurant has served"""
    self.customers_served = customers

  def increment_number_served(self, number_served):
    """Adds number to served guests"""
    self.customers_served += number_served
    print(f"We have served {number_served} new customers today!")
    print(f"We have served a total of: {self.customers_served} customers!")


class IceCreamStand(Restaurant):
  """Represents an icecream stand"""

  def __init__(self, name, cuisine_type='ice cream'):
    """Initialize an ice cream stand"""
    super().__init__(name, cuisine_type)
    self.flavors = []

  def show_flavors(self):
    """Display available flavors"""
    print("\nWe have the following flavors available:")
    for flavor in self.flavors:
      print(f"- {flavor.title()}")


pizza_palace = Restaurant('Pizza Palace', 'pizza')
print(f"{pizza_palace.name}, {pizza_palace.cuisine}")
pizza_palace.describe_restaurant()
pizza_palace.open_restaurant()

kepbap_shop = Restaurant('Kebap Shop', 'Turkish')
kepbap_shop.describe_restaurant()
kepbap_shop.open_restaurant()

golden_dragon = Restaurant('Golden Dragon', 'Chinese')
golden_dragon.describe_restaurant()
golden_dragon.open_restaurant()
golden_dragon.set_number_served(200)
golden_dragon.increment_number_served(30)


cold_confections = IceCreamStand('Cold Confections')
cold_confections.flavors = ['vanilla', 'chocolate', 'mint']

cold_confections.describe_restaurant()
cold_confections.show_flavors()