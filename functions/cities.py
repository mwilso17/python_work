# Mike Wilson 17 June 2021
# This program describes various cities using a function.

def describe_city(name, country='germany'):
  """prints name of city and country"""
  print(f"{name.title()} is located in {country.title()}")

describe_city('berlin')
describe_city('oldenburg')
describe_city('paris', 'france')
describe_city(country='spain', name='madrid')