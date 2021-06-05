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

print("\nTurns out that I only have enough room for 2 people.")

uninvited_guest = guests.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guests.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guests.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guests.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")

uninvited_guest = guests.pop()
print(f"Sorry, {uninvited_guest.title()}. There isn't enough room.")