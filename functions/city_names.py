# Mike Wilson 20 June 2021
# This program has a function that takes a city and country name and returns
# a string.

def city_name(city, country):
  """Return a string for a city, country pair"""
  return f"{city.title()}, {country.title()}"

city = city_name('berlin', 'germany')
print(city)

city = city_name('olso', 'norway')
print(city)

city = city_name('paris', 'france')
print(city)