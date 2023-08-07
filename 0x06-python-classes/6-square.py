#!/usr/bin/python3
"""Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A new square

    Args:
        size: the size of the number
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if type(size) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(size[0]) and type(size[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """computes the area of the square

        Args:
            self

        Returns:
            Area of the square
        """
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        for a in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for b in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.size):
                print('#', end='')
            print()
