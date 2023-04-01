#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == '__main__':
    if sys.arv[1]:
        q = sys.argv[1]
    else:
        q = ""

    payload = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", json=payload)

    try:
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print('[{}] {}'.format(res["id"], res["name"]))
    except:
        print("Not a valid JSON")
