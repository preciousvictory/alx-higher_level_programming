#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{a} + {b} = {ans}".format(a=a, b=b, ans=add(a, b)))
    print("{a} - {b} = {ans}".format(a=a, b=b, ans=sub(a, b)))
    print("{a} * {b} = {ans}".format(a=a, b=b, ans=mul(a, b)))
    print("{a} / {b} = {ans}".format(a=a, b=b, ans=div(a, b)))
