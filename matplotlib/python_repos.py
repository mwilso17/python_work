# Mike Wilson 13 July 2021
# A program to call API responses for GitHub.com

import requests

# Make an API call and store the responses.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stats'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())