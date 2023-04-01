#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and display
the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    try: urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
