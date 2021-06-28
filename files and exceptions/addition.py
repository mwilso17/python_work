# Mike Wilson 28 June 2021
# This program takes user input for 2 numbers and adds them together.
# It contains exceptions in case the user does not enter numbers.

try:
  x = input("Enter a number: ")
  x = int(x)

  y = input("Enter another number: ")
  y = int(y)

except ValueError:
  print("Please enter a number. ex: 3")

else:
  sum = x + y
  print(f"The sum of {x} and {y} is {sum}.")