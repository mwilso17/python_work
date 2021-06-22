# Mike Wilson 22 June 2021
# This program demonstrates how to import from another file. This program
# imports from restaurant.py.

from restaurant import Restaurant

my_restaurant = Restaurant('pizza mania', 'pizza')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()