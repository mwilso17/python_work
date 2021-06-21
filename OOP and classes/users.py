# Mike Wilson 20 June 2021
# this program simulates the creation of a user profile.

class User:
  """create a user profile"""

  def __init__(self, first, last, user_name):
    """initialize self and attributes"""
    self.first = first
    self.last = last
    self.user_name = user_name
    self.login_attempts = 0

  def describe_user(self):
    """describes the user"""
    print(f"\nFirst Name: {self.first.title()}")
    print(f"Last Name: {self.last.title()}")
    print(f"Username: {self.user_name}")

  def greet_user(self):
    """greets the user"""
    print(f"Welcome, {self.first.title()}!")

  def increment_login_attempts(self):
    """Increases the login_attempts by 1"""
    self.login_attempts += 1

  def reset_login_attempts(self):
    """Resets login_attempts to 0"""
    self.login_attempts = 0


class Admin(User):
  """Admin class profile with privileges."""

  def __init__(self, first, last, user_name):
    """Initializes attributes"""
    super().__init__(first, last, user_name)

    self.privileges = Privileges()


class Privileges():
  """A class to store an admin's privileges"""

  def __init__(self, privileges=[]):
    self.privileges = privileges

  def show_privileges(self):
    print("\nPrivileges:")
    if self.privileges:
      for privilege in self.privileges:
        print(f"- {privilege}")
    else:
      print("- This user has no privileges.")


my_user = User('mike', 'wilson', 'mikwil99')
my_user.describe_user()
my_user.greet_user()

their_user = User('bill', 'roberts', 'bilrob12')
their_user.describe_user()
their_user.increment_login_attempts()
their_user.increment_login_attempts()
print(f"  Login Attempts: {their_user.login_attempts}")
print("Resetting Login Attempts...")
their_user.reset_login_attempts()
print(f"  Login Attempts: {their_user.login_attempts}")
their_user.greet_user()


bill = Admin('bill', 'lee', 'billee22')
bill.describe_user()

bill.privileges.show_privileges()


print("\nAdding privileges...")
bill_privileges = [
  'can reset passwords',
  'can delete user',
  'can add new user',
]

bill.privileges.privileges = bill_privileges
bill.privileges.show_privileges()