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
        super().__init__(Rectangle)

        self.width = size
        self.height = size

    def __str__(self):
        """ overloading __str__ method should return [Square] (<id>) <x>/<y>
        - <size> width or height
        """
        return '[Square] {} {}/{} - {}\
                '.format(self.id, self.x, self.y, self.width)
