# Mike Wilson 14 June 2021
# This program is a copy of glossary.py but uses a loop and sorts them
# alphabetically.

glossary = {
  'boolean': 'an expression that can be evaluated as either true or false.',
  'string': 'a series of characters.',
  'dictionary': 'a set of key value pairs.',
  'function': 'a block of code that performs a task.',
  'list': 'a collection of items in a certain order.',
}

for word, definition in sorted(glossary.items()):
  print(f"\n{word.title()}: {definition}")