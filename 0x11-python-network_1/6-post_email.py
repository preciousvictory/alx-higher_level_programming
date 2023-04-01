#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response"""


if __name__ == "__main__":
    import sys
    import requests

    payload = {"email": sys.argv[2])
    url = sys.argv[1]

    r = requests.post(url, data=payload)
    print(r.text)
