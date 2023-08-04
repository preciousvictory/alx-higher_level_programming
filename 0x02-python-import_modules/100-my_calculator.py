#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    operator = '+-*/'
    if argv[2] not in operator:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    ans = 0
    if argv[2] == '+':
        ans = add(a=int(argv[1]), b=int(argv[3]))
    elif argv[2] == '-':
        ans = sub(a=int(argv[1]), b=int(argv[3]))
    elif argv[2] == '*':
        ans = mul(a=int(argv[1]), b=int(argv[3]))
    elif argv[2] == '/':
        ans = div(a=int(argv[1]), b=int(argv[3]))

    print(f'{argv[1]} {argv[2]} {argv[3]} = {ans}')
