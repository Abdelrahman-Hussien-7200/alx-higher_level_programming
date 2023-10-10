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