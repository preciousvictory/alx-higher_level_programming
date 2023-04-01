#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and display
the body of the response"""
import sys
import requests


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.HTTPError as err:
        print('Error code: {}'.format(err))
