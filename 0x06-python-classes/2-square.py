#!/usr/bin/python3
"""Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A new square

    Args:
        size: the size of the number
    """
    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
        else:
            self.__size = size
