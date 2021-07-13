# Mike Wilson 13 July 2021
# A hn article api call.

import requests
import json

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'matplotlib\data\creadable_hn_data.json'
with open(readable_file, 'w') as f:
  json.dump(response_dict, f, indent=4)