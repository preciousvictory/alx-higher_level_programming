#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    @staticmethod
    def validation(att, value):
        """
        adding validation of all setter methods and instantiation
        (id excluded)
            - If the input is not an integer, raise the TypeError exception
            with the message: <name of the attribute> must be an integer.
            Example: width must be an integer
            - If width or height is under or equals 0, raise the ValueError
            exception with the message: <name of the attribute> must be > 0.
            Example: width must be > 0
            - If x or y is under 0, raise the ValueError exception with the
            message: <name of the attribute> must be >= 0.
            Example: x must be >= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(att))
        if att == "x" or att == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(att))
        elif att == "width" or att == "height":
            if value <= 0:
                raise ValueError("{} numst be > 0".format(att))

    def area(self):
        """
        public method that returns the area value of the Rectangle instance.
        """
        return self.height * self.width

    def display(self):
        """
        public method  that prints in stdout the Rectangle instance with the
        character '#' by taking care of x and y
        note: x and y is like coordinates (x,y)
        """
        for y_ in range(self.y):
            print()
        for h in range(self.height):
            for x_ in range(self.x):
                print(" ", end='')
            for w in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """
        overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def update(self, *args,  **kwargs):
        """
         public method
         args - that assigns an argument to each attribute
             1st argument should be the id attribute
             2nd argument should be the width attribute
             3rd argument should be the height attribute
             4th argument should be the x attribute
             5th argument should be the y attribute

        kwargs - that assigns a key/value argument to attributes:
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        public method  that returns the dictionary representation of a
        Rectangle
        [Rectangle] (1) 1/9 - 10/2
        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        """
        return {
                "id": self.id,
                "width": self.widdth,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
