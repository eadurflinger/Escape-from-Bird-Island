import requests
usernames = []
response = requests.get('https://api.github.com/search/users?q=location:youngstown&per_page=100')
# print response.json()["items"][0]["login"]
items = response.json()["items"]
for item in items:
    usernames.append(item["login"])

print
