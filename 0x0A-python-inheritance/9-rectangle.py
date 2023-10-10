#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"