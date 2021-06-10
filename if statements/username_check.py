# Mike Wilson 10 June 2021
# This program simulates how a website verifies that every user has a unique
# username.

current_users = ['mike', 'bob', 'sally', 'bob2', 'jeff']
new_users = ['bob', 'mike', 'josh', 'ash', 'danny']

for new_user in new_users:
  if new_user in current_users:
    print(f"Sorry, but the username: {current_users} is already taken.")
  else:
    print(f"{new_user} is available as a username!")