# Mike Wilson 5 June 2021
# This program demonstrates various ways to manipulate a list and simulates
# a dinner party experience. A special thanks to all the Greats involved 
# and a certain Terrible one.

guest_list = ['Catherine', 'Frederick', 'Alexander', 'Ivan']
message = 'would you like to come to a great dinner party?'
print(f"{guest_list[0].title()}, {message}")
print(f"{guest_list[1].title()}, {message}")
print(f"{guest_list[2].title()}, {message}")
print(f"{guest_list[3].title()}, {message}")

print(f"\n{guest_list[3].title()} can't make it. It's terrible!")
del(guest_list[3])
print("\nMaybe Charles can come instead?")
guest_list.insert(3, 'charles')
print(f"\n{guest_list[0].title()}, {message}")
print(f"{guest_list[1].title()}, {message}")
print(f"{guest_list[2].title()}, {message}")
print(f"{guest_list[3].title()}, {message}")

print("\nWe found a bigger table! Let's invite more people")

