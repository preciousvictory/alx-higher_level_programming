#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integer"""
    for i in matrix:
        print(' '.join('{:d}'.format(j) for j in i))
