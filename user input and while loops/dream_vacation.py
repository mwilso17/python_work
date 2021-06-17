# Mike Wilson 17 June 2021
# The following program polls users about their dream vacations.

# 3 prompts to be used
name_prompt = "\nWhat is your name? "
vacation_prompt = "If you could vacation anywhere in the world, where would you go? "
next_prompt = "\nWould someone else like to take the poll? (yes/no)"

# empty dictionary to store responses in
responses = {}

while True:
  name = input(name_prompt)
  vacation = input(vacation_prompt)

  responses[name] = vacation

  repeat = input(next_prompt)
  if repeat != 'yes':
    break

print("\n-------Results-------")
for name, place in responses.items():
  print(f"{name.title()} would like to vacation to {place.title()}.")