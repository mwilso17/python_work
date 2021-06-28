# Mike Wilson 28 June 2021
# This program analyzes txt files for common words. The file used in this
# example comes from gutenberg.org, all rights reserved. This program is to be
# used strictly for educational and informational purposes.

def count_common_words(filename, word):
  """Counts how many time a word appears in a txt file."""
  try:
    with open(filename) as f:
      contents = f.read()

  except FileNotFoundError:
    pass

  else:
    word_count = contents.lower().count(word)

    message = f"'{word}' appers in {filename} around {word_count} times."