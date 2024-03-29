#!/usr/bin/python3
"""Square that defines a square by: (based on 3-square.py)"""


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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """computes the area of the square

        Args:
            self

        Returns:
            Area of the square
        """
        return self.__size**2
