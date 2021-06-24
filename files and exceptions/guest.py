# Mike Wilson 24 June 2021
# This program prompts a user for their name then writes it to
# txt_files\guest.txt.

name = input("What's your name? ")

filename = 'txt_files\guest.txt'

with open(filename, 'w') as f:
  f.write(name)