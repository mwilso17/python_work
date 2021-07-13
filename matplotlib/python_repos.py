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
print(f"Total repositiories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
  print(f"Name: {repo_dict['name']}")
  print(f"Owner: {repo_dict['owner']['login']}")
  print(f"Stars: {repo_dict['stargazers_count']}")
  print(f"Repository: {repo_dict['html_url']}")
  print(f"Created: {repo_dict['created_at']}")
  print(f"Updated: {repo_dict['updated_at']}")
  print(f"Description: {repo_dict['description']}")