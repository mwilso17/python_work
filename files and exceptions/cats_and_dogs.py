# Mike Wilson 28 June 2021
# This program analyzes two different txt files from the txt_files folder.
# This code catches the FileNotFound error.

filenames = ['txt_files\cats.txt', 'txt_files\dogs.txt']

for filename in filenames:
  try:
    with open(filename) as f:
      contents = f.read()

  except FileNotFoundError:
    pass

  else:
    print(f"\nReading file: {filename}")
    print(contents)
