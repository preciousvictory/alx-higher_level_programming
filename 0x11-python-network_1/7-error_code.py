#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and display
the body of the response"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
