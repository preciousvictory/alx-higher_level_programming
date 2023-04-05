#!/usr/bin/python3
""" a Python script that  Please list 10 commits (from the most recent to
oldest) of the repository “rails” by the user “rails”"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],sys.argv[1])
    commit = requests.get(url).json()
    i = 0
    for res in commit:
        if i < 10:
            print('{}: '.format(res['sha'], res.get('commit').get('author').get('name')))
        else:
            break
        i += 1
