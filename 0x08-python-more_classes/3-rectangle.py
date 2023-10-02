#!/usr/bin/python3

"""
An empty class Rectangle
"""


class Rectangle:
    """ Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Init  Rectangle."""

        self.width = width
        self.height = height

    def __str__(self):
        """Returns an readable string"""

        if self.__height == 0 or self.__width == 0:
            return ''
        put_hash = ''
        for i in range(self.__height):
            for j in range(self.__width):
                put_hash += '#'
            put_hash += '\n'
        return put_hash[:-1]

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ define the width function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        parameters:
            value: value of height,integer, positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area
        Returns:
            Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter
        Returns:
            Perimeter 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
