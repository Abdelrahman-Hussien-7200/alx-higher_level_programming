#!/usr/bin/python3

"""
An empty class Rectangle
"""


class Rectangle:
    """ Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init  Rectangle."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an readable string"""

        if self.__height == 0 or self.__width == 0:
            return ''
        put_hash = ''
        for i in range(self.__height):
            for j in range(self.__width):
                put_hash += str(self.print_symbol)
            put_hash += '\n'
        return put_hash[:-1]

    def __repr__(self):
        """Return internal string"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """get biggest Rectangle according to area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new instwidth == height == size"""
        return cls(size, size)
