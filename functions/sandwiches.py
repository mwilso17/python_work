# Mike Wilson 20 June 2021
# This program has a function that accepts the items someone may want on a 
# sandwich and prints them.

def make_sandwiches(*items):
  """make a sandwich"""
  print("\nI'll make you a sandwich")
  for item in items:
    print(f"  ... adding {item} to your sandwich")
    print("Your sandwich is ready!")


make_sandwiches('roast beef', 'chedder', 'lettuce')
make_sandwiches('turkey', 'ham', 'swiss')
make_sandwiches('peanut butter', 'fried bananas', 'honey')
