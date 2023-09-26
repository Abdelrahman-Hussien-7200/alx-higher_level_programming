#!/usr/bin/python3
"""Square class implemntation"""


class Square:
    """Square class code next"""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): Private instance attribute.
        """
        self.size = size

    @property
    def size(self):
        """return new size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return (self.__size * self.__size)
