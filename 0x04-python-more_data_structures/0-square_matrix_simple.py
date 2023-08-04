#!/usr/bin/python3
def square(n):
    return n * n


def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_list = []
    for i in matrix:
        result = map(square, i)
        new_list.append(list(result))
    return new_list
