# Mike Wilson 17 June 2021
# This program simulates a t-shirt maker using a function to accept
# arguments to make a certain sized shirt with a message on it.

def make_shirt(size='large', message='I love Python!'):
  """make the shirt with a message on it"""
  print(f"Making your {size} shirt that says '{message}'.")

# call function with positional arguments
make_shirt('small', 'I love ATL')

# call function with keyword arguments
make_shirt(size='medium', message='Python is fun!')

# calling function multiple times
make_shirt()
make_shirt()
make_shirt(size='x-large')
make_shirt(size='x-small', message='Functions are cool!')