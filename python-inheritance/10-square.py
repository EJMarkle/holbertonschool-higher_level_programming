#!/usr/bin/python3
""" defines a class square from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
