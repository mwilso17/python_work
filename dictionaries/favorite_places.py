# Mike Wilson 15 June 2021
# This program uses a dictionary to print people's favorite places.

favorite_places = {
  'mike': ['munich', 'kyoto', 'atlanta'],
  'ash': ['berlin', 'paris', 'london'],
  'rob': ['phoenix', 'sydney', 'olso'],
}

for name, places in favorite_places.items():
  print(f"\n{name.title()}'s favorite places are: ")
  for place in places:
    print(f"{place.title()}")