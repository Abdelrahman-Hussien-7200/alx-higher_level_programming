#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes:first_name, last_name
,age
"""


class Student:
    """class a student."""

    def __init__(self, first_name, last_name, age):
        """
            Initialize the class Student.
            first_name (str): The first name for student.
            last_name (str): The last name for student.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.

        If attrs is a list of strings, only attribute names 
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__