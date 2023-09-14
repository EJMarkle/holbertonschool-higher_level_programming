#!/usr/bin/python3
# 3-square.py
# Evan Markle
# Usage:
""" This class for Square is updated to unclude a size attribute. """


class Square:
    """ This is where the size attribute is updated """
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    """ This calculates the area of the given square. """
    def area(self):
        return (self.__size * self.__size)
