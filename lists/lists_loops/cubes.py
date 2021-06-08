# Mike Wilson 8 June 2021
# # This program makes a list of the cubed values of the numbers 1-10

# The following code demonstrates 1 way to write a program that cubes the correct numbers
cubes = []

for value in range(1, 11):
  cube = value ** 3
  cubes.append(cube)

print(cubes)

# The above code can be refactored to shorten the number of lines used
cubes = []

for value in range(1, 11):
  cubes.append(value**3)

print(cubes)