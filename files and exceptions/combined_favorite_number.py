# Mike Wilson 29 June 2021
# This program combines the code from read_favorite_number.py and
# favorite_number.py. 

import json

try:
  with open('json\\favorite_number2.json') as f:
    number = json.load(f)
except FileNotFoundError:
  number = input("What is your favorite number? ")
  with open('json\\favorite_number2.json', 'w') as f:
    json.dump(number, f)
  print("Ok. I will remember that.")
else:
  print(f"I remember your favorite number. It is {number}.")