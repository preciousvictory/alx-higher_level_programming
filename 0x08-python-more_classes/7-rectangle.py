#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """A new rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - retrieving  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - setting width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter - retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter - setting Width"""
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
        """print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
