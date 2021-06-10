# Mike Wilson 10 June 2021
# This program simulates how a website verifies that every user has a unique
# username.

current_users = ['mike', 'Bob', 'sally', 'bob2', 'Jeff']
new_users = ['bob', 'Mike', 'josh', 'ash', 'danny']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
  if new_user.lower() in current_users_lower:
    print(f"Sorry, but the username: '{new_user}' is already taken.")
  else:
    print(f"{new_user} is available as a username!")