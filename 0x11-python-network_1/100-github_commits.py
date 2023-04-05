#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
            .format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()

    for r in commits:
        print(r.get('sha'), end=': ')
        print(r.get('commit').get('author').get('name'))
