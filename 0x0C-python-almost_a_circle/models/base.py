#!/usr/bin/python3
"""
Base class and methods
"""
import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
         returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
