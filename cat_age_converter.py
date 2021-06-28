# Mike Wilson 26 June 2021
# This program converts 'human years' into 'cat years'.

# Human year age.
my_age = 30

# A value for the earlier years of a cat's life where they 'age' faster.
early_years = 2

# multiply by 25 because cats age faster in their fist 2 years of life.
early_years *= 25

# after 2 years, cats age slower, so we subtract the 2 years accounted for earlier
later_years = my_age - 2

# multiply later years by 4.
later_years *= 4

my_age_in_cat_years = later_years + early_years

print(f" My age in cat years is: {my_age_in_cat_years}")