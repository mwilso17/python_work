# Mike Wilson 15 June 2021
# This program has cities in a dictionary and prints data stored in each
# city's dictionary. (Nested dictionaries)

cities = {
  'atlanta': {
    'country': 'the USA',
    'population': 1_000_000,
    'fact': 'is home to Coca-Cola.',
  },
  'carrollton': {
    'country': 'the USA',
    'population': 15_000,
    'fact': 'is home to Southwire.',
  },
  'oldenburg': {
    'country': 'Germany',
    'population': 100_000,
    'fact': 'is over 600 years old!'
  },
}

for city, city_info in cities.items():
  country = city_info['country']
  population = city_info['population']
  fact = city_info['fact']

  print(f"\n{city.title()} is in {country}.")
  print(f"  It has a population of about {population}.")
  print(f"  {city.title()} {fact}")