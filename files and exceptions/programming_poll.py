# Mike Wilson 24 June 2021
# This program uses a while loop to ask people why the enjoy programming.
# Responses are stored in 'txt_files\programming_poll.txt'.

filename = 'txt_files\programming_poll.txt'

responses = []
while True:
  response = input("\nWhy do you like programming? ")
  responses.append(response)

  continue_poll = input("Would you like to let someone else respond? (y/n) ")
  if continue_poll != 'y':
    break

with open(filename, 'a') as f:
  for response in responses:
    f.write(f"{response}\n")