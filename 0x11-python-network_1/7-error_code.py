#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python 7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()

    print(response.text)
except requests.exceptions.RequestException as e:
    if hasattr(e.response, 'status_code'):
        print("Error code:", e.response.status_code)
    else:
        print("Error sending the request:", e)
