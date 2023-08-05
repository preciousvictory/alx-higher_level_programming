#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    ans = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)"""
    if not my_list:
        return 0

    scores = 0
    weight = 0
    for grade in my_list:
        scores += (grade[0] * grade[1])
        weight += grade[1]
    return scores / weight
