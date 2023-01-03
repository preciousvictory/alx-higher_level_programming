#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """A new rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.__width)]
            #rect.append('#'*self.width)
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))
