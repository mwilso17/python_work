# Mike Wilson 20 June 2021
# This program has a list of short messages and displays them.

def show_messages(messages):
  """print messages in  list"""
  for message in messages:
    print(message)

def send_messages(messages, sent_messages):
  """print each message and move it to sent messages"""
  print("\nSending all messages")
  while messages:
    current_messages = messages.pop()
    print(current_messages)
    sent_messages.append(current_messages)    

messages = ['hey!', 'What\'s up?', ':)']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)