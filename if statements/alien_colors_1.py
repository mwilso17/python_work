# Mike Wilson 10 June 2021
# This program simulates an alien spaceship being shot down by the player
# and prints a message giving points based on the color of the spaceship.

alien_color = 'red' #this variable can be changed to green, yellow, or another color

if alien_color == 'green':
  print("You earned 5 points!")
elif alien_color == 'yellow':
  print("You earned 10 points!")
else:
  print("You earned 15 points!")
