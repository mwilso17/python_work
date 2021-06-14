# Mike Wilson 14 June 2021
# This program has several dictionaries and prints details of each one using
# a single 'for' loop when nesting them inside of a list.

# Empty dictionary to store other dictionaries in.
pets = []

# Dictionaries containing info about people's pets.
pet = {
  'name': 'mia',
  'owner': 'mike',
  'age': 1,
  'species': 'ball python',
}
pets.append(pet)

pet = {
  'name': 'spaz',
  'owner': 'rob',
  'age': 3,
  'species': 'cat'
}
pets.append(pet)

pet = {
  'name': 'bobba'
  'owner': 'alice'
  'age': 5,
  'species': 'ferret'
}
pets.append(pet)
