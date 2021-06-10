# Mike Wilson 10 June 2021
# This program uses an if-elif-else chain to print a message based on someone's
# age.

age = 2  #age can be changed to whatever number is desired. 

if age <= 1:
  print("You are a baby.")
elif age <= 3:
  print("You are a toddler.")
elif age <= 12:
  print("You are a kid.")
elif age <= 19:
  print("You are a teenager.")
elif age <= 64:
  print("You are an adult.")
else:
  print("You are an elder.")
