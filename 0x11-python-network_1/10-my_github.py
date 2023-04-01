#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password
and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user])

    response = requests.get(uri, auth=(user, passwd))
    print(reponse.json().get('id')
