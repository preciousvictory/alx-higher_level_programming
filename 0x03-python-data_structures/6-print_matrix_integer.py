#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integer"""
    for i in matrix:
        for j in range(len(i) + 1):
            if j % 2 != 0:
                i.insert(j, " ")
        txt = ""
        for j in i: 
            txt += '{}'.format(j)
        print(txt)
