#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == '__main__':
    let = "" if len(sys.argv) == 1 else sys.argv[1]

    payload = {"q": let}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print('[{}] {}'.format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
