# Mike Wilson 20 June 2021
# This program builds a dictionary discribing an album. Code has been updated
# to allow users to enter in data.

def make_album(artist, title, tracks=0):
  """Build a dictionary containing info about an album"""
  album_dictionary = {
    'artist': artist.title(),
    'title': title.title(),
  }
  if tracks:
    album_dictionary['tracks'] = tracks
  return album_dictionary

# Prepare prompts
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "\nWho is the artist? "

# Let the user know how to exit program.
print("Enter 'quit' anytime to stop the program.")

while True:
  title = input(title_prompt)
  if title == 'quit':
    break

  artist = input(artist_prompt)
  if artist == 'quit':
    break

  album =make_album(artist, title)
  print(album)

print("\nThanks for responding!")