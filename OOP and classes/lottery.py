# Mike Wilson 22 June 2021
# This program simulates a lottery and displays the 'winning' combination.

from random import choice

possibilities = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("And the winning ticket is...... ")

# While loop to keep numbers and letters from repeating.
while len(winning_ticket) < 4:
  pulled_item = choice(possibilities)

  #Only adds pulled item to winning_ticket if not yet pulled
  if pulled_item not in winning_ticket:
    winning_ticket.append(pulled_item)


