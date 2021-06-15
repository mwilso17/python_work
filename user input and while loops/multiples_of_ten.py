# Mike Wilson 15 June 2021
# This program asks the user to input a number and returns if that number is a
# multiple of 10 or not.

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
  print(f"\nThe number {number} is divisible by 10.")
else:
  print(f"\nThe number is not divisible by 10.")