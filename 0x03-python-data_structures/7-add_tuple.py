#!/usr/bin/python3
def check(t):
    try:
        a = t[0]
    except:
        a = 0
    try:
        b = t[1]
    except:
        b = 0
    return (a, b)

def add_tuple(tuple_a=(), tuple_b=()):
    """
     a function that adds 2 tuples.
     Returns a tuple with 2 integers:
    """
    a = check(tuple_a)
    b = check(tuple_b)

    return (a[0] + b[0], a[1] + b[1])
