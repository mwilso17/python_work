# Mike Wilson 22 June 2021
# This program reads the file learning_python.txt contained in this folder.


print("--- Reading the entire file:")
with open('learning_python.txt') as f:
  contents = f.read()
print(contents)