# Mike Wilson 10 June 2021
# This program loops through a list to print a greeting for each user.
# There is also a special greeting for the admin.

users = ['admin', 'marshall', 'lilly', 'ted', 'robin']

if users:  
  for name in users:
   if name == 'admin':
     print('Hello admin. Would you like to see a status report?')
   else:
      print(f"Hello {name.title()}. How are you doing today?")
else:
  print("We need to find some users!")