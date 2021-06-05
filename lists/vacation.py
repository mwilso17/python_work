# Mike Wilson 5 June 2021
# This program manipulates a list in various ways.

vacation_places = ['peru', 'germany', 'brazil', 'canada', 'iceland']

# printing list in origional order
print(vacation_places)

# sorts the list alphabetically without changing the contents of the list
print(sorted(vacation_places))

# reverse alphabetical list
print(sorted(vacation_places, reverse=True))

# showing that the origional list is still in its origional order
print(vacation_places)

# reversing the origional order of the list
vacation_places.reverse()
print(vacation_places)