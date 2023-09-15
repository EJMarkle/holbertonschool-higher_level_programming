#!/usr/bin/python3
# 4-square.py
# Evan Markle
# Usage:
""" This class for Square is updated to unclude a size attribute. """


class Square:
    """ This is where the size attribute is updated """
    def __init__(self, size=0):
        self.__size = size
    
    """ This retrieves the size of the square """
    @property
    def size(self):
        return self.__size

    """ This sets the size of the square """
    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """ This calculates the area of the given square. """
    def area(self):
        return self.__size * self.__size
