# Mike Wilson 11 July 2021
# This program explores data from a json file.

import json
from os import read

# Explore the structure of the data
filename = 'matplotlib\data\eq_data_1_day_m1.json'
with open(filename) as f:
  all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
  mag = eq_dict['properties']['mag']
  lon = eq_dict['geometry']['coordinates'][0]
  lat = eq_dict['geometry']['coordinates'][1]
  mags.append(mag)
  lons.append(lon)
  lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])