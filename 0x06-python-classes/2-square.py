#!/usr/bin/python3
# 2-square.py
"""a class Square that defines a square."""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        """Square class contructor
        Args:
            size (int): Private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
