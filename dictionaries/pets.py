# Mike Wilson 14 June 2021
# This program has several dictionaries and prints details of each one using
# a single 'for' loop when nesting them inside of a list.

# Empty dictionary to store other dictionaries in.
pets = []

# Dictionaries containing info about people's pets.
pet = {
  'name': 'mia',
  'owner': 'mike',
  'age': 12,
  'species': 'ball python',
}
pets.append(pet)

pet = {
  'name': 'spaz',
  'owner': 'rob',
  'age': 3,
  'species': 'cat',
}
pets.append(pet)

pet = {
  'name': 'bobba',
  'owner': 'alice',
  'age': 5,
  'species': 'ferret',
}
pets.append(pet)

# create a for loop to list all the details we know about the pets.
for pet in pets:
  name = pet['name'].title()
  owner = pet['owner'].title()
  age = pet['age']
  species = pet['species']

  print(f"{name} is a {species} and is {age} years old. {owner} loves them alot!")