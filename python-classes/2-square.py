#!/usr/bin/python3
# 2-square.py
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
