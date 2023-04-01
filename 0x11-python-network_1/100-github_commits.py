#!/usr/bin/python3
""" a Python script that  Please list 10 commits (from the most recent to
oldest) of the repository “rails” by the user “rails”"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}/{}'.format(sys.argv[1])
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=auth)
