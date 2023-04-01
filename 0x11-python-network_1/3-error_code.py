#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and display
the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))

    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
