# Mike Wilson 20 June 2021
# This program is specifically used to be imported to printing_models.py.
# These functions simulate a 3d printer.


def print_models(unprinted_designs, completed_models):
  """Simulate printing each design"""
  while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate a printed item from the 3d printer
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)