# Mike Wilson 14 June 2021
# This program has a dictionary and loops through its contents.
# Afterwards, it prints the key value pairs.

rivers = {
  'germany': 'rhine',
  'egypt': 'nile',
  'china': 'yellow',
}

for country, river in rivers.items():
  print(f"\nThe {river.title()} river runs through {country.title()}.")

print("The following rivers can be found in the dictionary:")
for river in rivers.values():
  print(f"{river.title()}")

