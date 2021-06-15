# Mike Wilson 15 June 2021
# This program simulates a party requesting a table at a busy restaurant.

#Code to get user input then convert it to a number
number_of_guests = input("How many people will be in your party tonight? ")
number_of_guests = int(number_of_guests)

if number_of_guests > 8:
  print("You will have to wait for a table. One should be ready soon.")
else:
  print("We have a table ready. Follow me!")