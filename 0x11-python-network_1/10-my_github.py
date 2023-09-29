#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python 10-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = f"https://api.github.com/user"

headers = {
    'Authorization': f'Basic {username}:{access_token}'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    user_data = response.json()
    if 'id' in user_data:
        print(user_data['id'])
    else:
        print("Unable to retrieve user ID.")
except requests.exceptions.RequestException as e:
    print("Error accessing GitHub API:", e)
