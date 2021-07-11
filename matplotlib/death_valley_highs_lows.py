# Mike Wilson 11 July 2021
# Program charting the high and low temps of Death Valley.

import csv

filename = 'matplotlib\data\death_valley_2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  for index, column_header in enumerate(header_row):
    print(index, column_header)