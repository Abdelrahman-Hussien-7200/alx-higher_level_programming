#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): Private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)