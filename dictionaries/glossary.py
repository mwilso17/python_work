# Mike Wilson 14 June 2021
# This program mimics an actual dictionary

glossary = {
  'boolean': 'an expression that can be evaluated as either true or false.',
  'string': 'a series of characters.',
  'dictionary': 'a set of key value pairs.',
  'function': 'a block of code that performs a task.',
  'list': 'a collection of items in a certain order.',
}

word = 'boolean'
print(f"\n{word.title()}: {glossary[word]}")

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

word = 'function'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")