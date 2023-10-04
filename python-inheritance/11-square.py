#!/usr/bin/python3
""" defines a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines class square that inherits rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
