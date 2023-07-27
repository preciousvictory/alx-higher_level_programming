#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    a function that prints all integers of a list, in reverse order."""
    if my_list is None:
        return
    for i in range(len(my_list), 0, -1):
        print("{:d}".format(i))
