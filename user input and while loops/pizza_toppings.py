# Mike Wilson 15 June 2021
# This program takes user input and simulates adding their input to a pizza.

prompt = "\nWhat type of toppings would you like on your pizza?"
prompt += "\nEnter 'quit' to stop. "


while True:
  toppings = input(prompt)
  if toppings != 'quit':
    print(f"Adding {toppings} to your pizza now!")
  else:
      print(f"Making your pizza now!")
      break