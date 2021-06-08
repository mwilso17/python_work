# Mike Wilson 8 June 2021
# This program slices from one list and adds it to another, while keeping
# two seperate lists that operate independantly of one another.

my_favorite_pizzas = ['pepperoni', 'deep dish', 'mushroom']
your_favorite_pizzas = my_favorite_pizzas[:]

print("My favorite pizzas are: ")
print(my_favorite_pizzas)

print("\nYou like many of the same pizzas I do!")
print("\nYour favorite pizzas are: ")
print(your_favorite_pizzas)

print("\n Let's add some more pizzas to our favorites.")

my_favorite_pizzas.append('extra cheese')
my_favorite_pizzas.append('salami')
your_favorite_pizzas.append('Detroit style')
your_favorite_pizzas.append('veggie')

print(my_favorite_pizzas)
print(your_favorite_pizzas)