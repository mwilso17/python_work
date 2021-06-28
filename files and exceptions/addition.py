# Mike Wilson 28 June 2021
# This program takes user input for 2 numbers and adds them together.
# It contains exceptions in case the user does not enter numbers.

print("Enter 'q' at ant time to quit.\n")

while True:
  try:
    x = input("Enter a number: ")
    if x == 'q':
      break
    x = int(x)

    y = input("Enter another number: ")
    if y == 'q':
      break
    y = int(y)

  except ValueError:
    print("Please enter a number. example: 3")

  else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")