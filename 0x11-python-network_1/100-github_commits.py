#!/usr/bin/python3
""" a Python script that  Please list 10 commits (from the most recent to
oldest) of the repository by the user"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'
    .format(argv[2], argv[1])
    commit = requests.get(url).json()
    for res in commit[:10]:
        print('{}: {}'
              .format(res['sha'], res.get('commit').get('author').get('name')))
