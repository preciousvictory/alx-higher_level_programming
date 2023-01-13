#!/usr/bin/python3
"""
Pascal's Triangle - returns a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    a function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascal’s triangle of n:
    """
    if n < 0:
        return []

    pas_tri = []
    for i in range(n):
        nth_list = []
        pas_tri.append(nth_list)
        nth_list.append(1)
        for j in range(1, i):
            nth_list.append(pas_tri[i - 1][j - 1] + pas_tri[i - 1][j])

        if i != 0:
            nth_list.append(1)

    return pas_tri
