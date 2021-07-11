# Mike Wilson 11 Jule 2021
# Read data from data folder.

import csv

filename = 'matplotlib\data\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  for index, column_header in enumerate(header_row):
    print(index, column_header)

  