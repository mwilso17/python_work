# Mike Wilson 14 June 2021
# This program stores people's favorite numbers and prints the key value pairs

favorite_numbers = {
  'Mike': [30, 15, 29],
  'Ash': [42, 22, 14],
  'John': [120, 222, 333],
  'Bill': [7, 2, 1],
  'Dan': [413, 16, 3],
}


for name, numbers in favorite_numbers.items():
  print(f"\n{name.title()}'s favorite numbers are: ")
  for number in numbers:
    print(f"{number}")
