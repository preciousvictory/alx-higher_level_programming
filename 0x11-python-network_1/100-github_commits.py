#!/usr/bin/python3
"""
a Python script that  Please list 10 commits (from the most recent to
oldest) of the repository by the user """
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"
    .format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    for res in commits[:10]:
        print('{}: {}'
              .format(res.get('sha'), res.get('commit').get('author').get('name')))
