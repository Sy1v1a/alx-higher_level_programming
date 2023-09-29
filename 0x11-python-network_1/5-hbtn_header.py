#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python 5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
except requests.exceptions.RequestException as e:
    print("Error fetching the URL:", e)
