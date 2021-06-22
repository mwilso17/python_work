# Mike Wilson 22 June 2021
# This program imports users.py and calls upon its class 'Admin'.

from users import Admin

mike = Admin('mike', 'wilson', 'mmwww2413')
mike.describe_user()

mike_privileges = [
  'can reset passwords',
  'can delete accounts',
]
mike.privileges.privileges = mike_privileges

mike.privileges.show_privileges()