# Mike Wilson 20 June 2021
# This program stores info about a car in  a dictionary. 

def make_car(make, model, *other):
  """makes a dictionary for a car"""
  car_dictionary = {
    'make': make.title(),
    'model': model.title(),
  }

  for other, value in other.items():
    car_dictionary[other] = value

  return car_dictionary

