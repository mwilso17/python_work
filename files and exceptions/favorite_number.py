# Mike Wilson 29 June 2021
# This program prompts a user for a favorite number and stores the data
# in a file that can later be retrieved.

import json

number = input("What is your favorite number? ")

with open('json\\favorite_number.json', 'w') as f:
  json.dump(number, f)
  print("Thanks. I will remember your favorite number.")