# Mike Wilson 14 June 2021
# This program creates a dictionary and adds a dictionary to it and uses a 
# 'for' loop to access the data within.

# Make an empty list to store people in.
people = []

# Define some people and add them to the list above.
person = {
  'name': 'mike',
  'city': 'atlanta',
  'age': 30,
}
people.append(person)

person = {
  'name': 'julian',
  'city': 'boston',
  'age': 28,
}
people.append(person)

person = {
  'name': 'rob',
  'city': 'houston',
  'age': '41'
}
people.append(person)

# Display info about people.
for person in people:
  name = person['name'].title()
  age = person['age']
  city = person['city'].title()

  print(f"{name} is {age} years old and lives in {city}.")