# Mike Wilson 20 June 2021
# this program simulates the creation of a user profile.

class User:
  """create a user profile"""

  def __init__(self, first, last, user_name):
    """initialize self and attributes"""
    self.first = first
    self.last = last
    self.user_name = user_name

  def describe_user(self):
    """describes the user"""
    print(f"\nFirst Name: {self.first.title()}")
    print(f"Last Name: {self.last.title()}")
    print(f"Username: {self.user_name}")

  def greet_user(self):
    """greets the user"""
    print(f"Welcome, {self.first.title()}!")