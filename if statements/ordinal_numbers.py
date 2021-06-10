# Mike Wilson 10 June 2021
# This program stores the values of numbers and gives their ordinal modifer.
# ie: 1 turns to 1st. 2 turns to 2nd, etc.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
  if number == 1:
    print("1st")
  elif number == 2:
    print("2nd")
  elif number == 3:
    print("3rd")
  else:
    print(f"{number}th")