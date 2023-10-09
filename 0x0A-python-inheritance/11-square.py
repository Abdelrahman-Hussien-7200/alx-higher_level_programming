#!/usr/bin/python3
"""
class square that inherits from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle
"""
class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    subsubclass square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
