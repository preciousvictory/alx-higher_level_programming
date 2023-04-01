#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password
and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]

    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(user, passwd))
    print(reponse.json().get('id'))
