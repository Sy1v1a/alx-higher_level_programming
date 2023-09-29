#!/usr/bin/python3
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python 1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get("X-Request-Id")
        print(x_request_id)
except urllib.error.URLError as e:
    print("Error fetching the URL:", e)
