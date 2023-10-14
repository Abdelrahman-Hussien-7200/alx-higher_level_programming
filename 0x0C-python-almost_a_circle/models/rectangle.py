#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
     class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init fuc
        """
        self.width = width
        self.heigth = heigth
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width
        """
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        """
        self.validation("height", value)
        self.height = value

    @property
    def x(self):
        """
        getter method for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x
        """
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
        getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y
        """
        self.setter_validation("y", value)
        self.__y = value
