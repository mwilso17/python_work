# Mike Wilson 5 June 2021
# This program demonstrates various ways to manipulate a list and simulates
# a dinner party experience. A special thanks to all the Greats involved 
# and a certain Terrible one.

guest_list = ['catherine', 'frederick', 'alexander', 'ivan']
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
guest_list.append('cnut')
guest_list.append('peter')
guest_list.append('llywelyn')

print(f"\n{guest_list[0].title()}, {message}")
print(f"{guest_list[1].title()}, {message}")
print(f"{guest_list[2].title()}, {message}")
print(f"{guest_list[3].title()}, {message}")
print(f"{guest_list[4].title()}, {message}")
print(f"{guest_list[5].title()}, {message}")
print(f"{guest_list[6].title()}, {message}")

# invited too many people. Using pop method to uninvite some people.
print("\nTurns out that I only have enough room for 2 people.")

uninvited_guest = guest_list.pop()
print(f"\nSorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guest_list.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

#inviting last 2 people to dinner
print(f"\n{guest_list[0].title()}, {message}")
print(f"{guest_list[1].title()}, {message}")

# empty the list
del(guest_list[0])
del(guest_list[0])

# prove the list is empty
print(guest_list)