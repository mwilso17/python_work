# Mike Wilson 29 June 2021
# This program reads the answer from favorite_number.py with the answer
# that was stored in the 'json' folder.

import json

with open('json\\favorite_number.json') as f:
  number = json.load(f)

print(f"I know your favorite number. It is {number}.")