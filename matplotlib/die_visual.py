# Mike Wilson 9 July 2021
# A visualization of the die class.

from die import Die

# Create a D6.
die = Die()

# Make some rolls and store the results in a list.
results = []
for roll_num in range(100):
  result = die.roll()
  results.append(result)

print(results)