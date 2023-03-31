#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:$')
        print(f'\t - typ3: {type(html)}')
        print(f'\t - content: {html}')
        print(f'\t - utf8 content: {html.decode("utf-8")}')
