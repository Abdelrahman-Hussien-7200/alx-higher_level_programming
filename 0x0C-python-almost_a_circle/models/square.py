#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
from models.base import Rectangle


Class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter width or height = size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for Square height and width
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Square readable output
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)