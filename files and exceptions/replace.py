# Mike Wilson 22 June 2021
# This program replaces a word in a txt document. Please view the folder
# 'txt_files' for the exact document used.

filename = 'txt_files\learning_python.txt'

print("--- Displaying unchanged file one time:")
with open(filename) as file:
  contents = file.read()
print(contents)

print("--- Now replacing a word in the file:")
with open(filename) as file:
  lines = file.readlines()

for line in lines:
  line = line.rstrip()
  print(line.replace('can', 'could'))