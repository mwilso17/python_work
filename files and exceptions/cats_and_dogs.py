# Mike Wilson 28 June 2021
# This program analyzes two different txt files from the txt_files folder.
# This code catches the FileNotFound error.

filenames = ['txt_files\cats.txt', 'txt_files\dogs.txt']

for filename in filenames:
  print(f"\nReading file: {filename}")
  try:
    with open(filename) as f:
      contents = f.read()
      print(contents)
    except FileNotFoundError:
      print("Sorry, but we cannot find that file.")