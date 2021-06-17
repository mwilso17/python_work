# Mike Wilson 17 June 2021
# This program simulates a sandwich shop that takes sandwich orders
# and moves them to a list of finished sandwiches.

# list for sandwich orders
sandwich_orders = ['club', 'ham and swiss', 'pastrami', 'turkey', 'veggie']

# empty list for finished sandwiches
finished_sandwiches = []

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  print(f"I am making your {current_sandwich} sandwich now.")
  finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
  print(f"Here is your {sandwich} sandwich.")  