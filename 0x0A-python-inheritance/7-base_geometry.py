#!/usr/bin/python3
"""
 class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """
    class BaseGeometry (based on 6-base_geometry.py)
    """
    def area(self):
        """
        only raise implementation error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method
        if value is not an integer: raise a TypeError exception
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message <name>
        must be greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
