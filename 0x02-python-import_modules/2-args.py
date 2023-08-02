#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    if length == 1:
        t = 'argument'
    else:
        t = 'arguments'
    print(f'{length} {t}', end='')
    if length == 0:
        print('.')
    else:
        print(':')

    n = 1
    for i in argv[1:]:
        print(f'{n}: {i}')
        n += 1
