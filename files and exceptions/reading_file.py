# Mike Wilson 22 June 2021
# This program reads the file learning_python.txt contained in this folder.

filename = 'txt_files\learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)