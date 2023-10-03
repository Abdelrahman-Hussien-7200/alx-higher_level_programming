#!/usr/bin/python3
""" a class LockedClass with no class or object attribute
prevents the user from dynamically creating new instance attributes, 
except if the new instance attribute is called first_name
"""


class LockedClass():
    """ first_name declarations """
    __slots__ = ('first_name')
