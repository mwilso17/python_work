# Mike Wilson 20 June 2021
# This program builds a dictionary containing info we know about a person.

def build_profile(first, last, **user_info):
  """Build a disctionary containing a person's info"""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

