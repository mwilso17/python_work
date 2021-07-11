# Mike Wilson 11 July 2021
# This program explores data from a json file.

import json
from os import read

# Explore the structure of the data
filename = 'matplotlib\data\eq_data_1_day_m1.json'
with open(filename) as f:
  all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))