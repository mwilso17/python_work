# Mike Wilson 15 June 2021
# This program takes user input for age then returns the price of their movie
# ticket to them.

prompt = "\nWhat is your age? "
prompt += "\nEnter 'quit' when you are finished."


while True:
  age = input(prompt)
  if age == 'quit':
    break
  age = int(age)

  if age < 3:
    print("Your ticket is free.")
  elif age < 12:
    print("Your ticket is $10.")
  elif age < 65:
    print("Your ticket is $15.")
  elif age < 400:
    print("You get a senior discount. Your ticket is $12.")
  elif age >= 400:
    print("Sorry, we don't let vampires into this theater.")