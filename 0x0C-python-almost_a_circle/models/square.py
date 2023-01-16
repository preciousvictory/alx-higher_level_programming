#!/usr/bin/python3
"""
class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
     the class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        The width and height must be assigned to the value of size
        All width, height, x and y validation must inherit from Rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validation('width', value)
        self.width = value
        self.height = value

    def __str__(self):
        """ overloading __str__ method should return [Square] (<id>) <x>/<y>
        - <size> width or height
        """
        return '[Square] ({}) {}/{} - {}\
                '.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ public method
        - *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        - **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        public method  that returns the dictionary representation of a
        Rectangle
        [Rectangle] (1) 1/9 - 10/2
        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        """
        return "\{'x': {}, 'y': {}, 'id': {}, 'height': {},'width': {}\
                ".format(self.x, self.y, self.id, self.size, self.size)
