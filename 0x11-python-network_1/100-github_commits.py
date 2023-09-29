#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python 100-github_commits.py <repository name> <owner name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

try:
    response = requests.get(url)
    response.raise_for_status()

    commits = response.json()
    # Print the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
except requests.exceptions.RequestException as e:
    print("Error accessing GitHub API:", e)
