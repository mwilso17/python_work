# Mike Wilson 24 June 2021
# This program uses a while loop to prompt users for their name and 
# prints a greeting. Entries are stored in 'txt_files\guest_book.txt'.

filename = 'txt_files\guest_book.txt'

print("Enter 'q' to exit the program")
while True:
  name = input("\nWhat is your name? ")
  if name == 'q':
    break
  else:
    with open(filename, 'a') as f:
      f.write(f"{name}\n")
    print(f"Hi {name.title()}. You have been added to the guest book!")