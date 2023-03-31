#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        resp = res.read()
        print('Body response:$')
        print(f'\t- typ3: {type(resp)}$')
        print(f'\t- content: {resp}$')
        print(f'\t- utf8 content: {resp.decode("utf-8")}$')
