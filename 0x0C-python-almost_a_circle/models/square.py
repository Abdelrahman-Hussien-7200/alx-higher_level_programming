#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        Args:
            size (int): The size Square.
            x (int): The x Square.
            y (int): The y Square.
            id (int): The identity Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter width or height = size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for Square height and width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update square props
        Args:
            *args (ints): New attribute values.
                - 1st argument id
                - 2nd argument size
                - 3rd argument x
                - 4th argument y
            **kwargs (dict): New key/value pairs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Square readable output
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
