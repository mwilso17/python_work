# Mike Wilson 14 June 2021
# This program has a dictionary and uses for loops with if statements in order
# to see if someone has taken a poll or not.

favorite_pizzas = {
  'mike': 'pepperoni',
  'danny': 'mushroom',
  'ash': 'cheese',
  'john': 'supreme'
}

for name, pizza in favorite_pizzas.items():
  print(f"{name.title()}'s favorite pizza is {pizza}.")

print("\n")

pizza_lovers = ['mike', 'bob', 'danny', 'john', 'christie', 'bill', 'john']

for person in pizza_lovers:
  if person in favorite_pizzas.keys():
    print(f"Thank you for taking the poll, {person.title()}!")
  else:
    print(f"What is your favorite pizza, {person.title()}?")