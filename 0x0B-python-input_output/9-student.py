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

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
