# Mike Wilson 20 June 2021
# This program imports printing_functions.py and calls upon its functions

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dice']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
