# Mike Wilson 20 June 2021
# This program has a list of short messages and displays them.

def show_messages(messages):
  """print messages in  list"""
  for message in messages:
    print(message)

messages = ['hey!', 'What\'s up?', ':)']
show_messages(messages)