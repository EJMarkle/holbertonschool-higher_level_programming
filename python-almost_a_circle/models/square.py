#!/usr/bin/python3
""" this is the square class! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns the string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ gets square size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates square params """
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns definition for square """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
