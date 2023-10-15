#!/usr/bin/python3
"""
Base class and methods
"""
import json


Class Base:
    """
    base calss
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init class constructor
        """
        if id is not None:
            self.id = None
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as abdofile:
            if list_objs is None:
                abdofile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                abdofile.write(cls.to_json_string(list_dicts))
