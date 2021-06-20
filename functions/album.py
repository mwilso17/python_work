# Mike Wilson 20 June 2021
# This program builds a dictionary discribing an album.

def make_album(artist, title, tracks=0):
  """Build a dictionary containing info about an album"""
  album_dictionary = {
    'artist': artist.title(),
    'title': title.title(),
  }
  if tracks:
    album_dictionary['tracks'] = tracks
  return album_dictionary

