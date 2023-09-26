#!/usr/bin/python3

"""class Square that defines a square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): size of new square.
            size is private attribute.
        """
        self.__size = size
