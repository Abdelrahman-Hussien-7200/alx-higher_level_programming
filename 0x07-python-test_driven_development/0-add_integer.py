#!/usr/bin/python3
"""
function thta return the sum of two numbers a, b
"""


def add_integer(a, b=98):

    """
    add_integer: add two numbers
    paramters:
        a - integer number
        b - integer number
    Return:
        sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError ("b must be an integer")
    return int(a) + int(b)
