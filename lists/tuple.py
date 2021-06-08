# Mike Wilson 8 June 2021
# This program shows an example of a tuple. The example is a small restaurant
# that has a menu of items that should not change.

menu = ('burgers', 'fries', 'chicken tenders', 'soda', 'ice cream')

for item in menu:
  print(f"This restaurant serves {item}.")

# Although you cannot modify a tuple, you can assign a new value to a 
# variable within a tuple.

menu = ('burgers', 'chips', 'chicken sandwichs', 'soda', 'ice cream')

for item in menu:
  print(f"This restaurant serves {item}.")