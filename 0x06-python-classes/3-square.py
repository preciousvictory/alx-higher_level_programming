#!/usr/bin/python3
"""Square that defines a square by: (based on 2-square.py)"""


class Square:
    """A new square

    Args:
        size: the size of the number
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """computes the area of the square

        Args:
            self

        Returns:
            Area of the square
        """
        return self.__size**2
