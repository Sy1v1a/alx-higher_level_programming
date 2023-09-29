#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()

    try:
        user_data = response.json()
        if user_data:
            print("[{}] {}".format(user_data['id'], user_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print("Error sending POST request:", e)
