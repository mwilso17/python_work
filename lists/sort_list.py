# Mike Wilson 5 June 2021
# This program demonstrates how to sort a few lists alphabetically and
# reverse alphabetically

instruments = ['guitar', 'violin', 'bass', 'drums', 'piano']

# prints the origional list
print(instruments)

# sorts alphabetically
instruments.sort()
print(instruments)

# Sorting a new list reverse alphabetically
vacation_destinations = ['germany', 'france', 'spain', 'russia', 'canada']
instruments.sort(reverse=True)
print(vacation_destinations.title())