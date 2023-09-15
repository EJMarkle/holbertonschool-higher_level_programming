#!/usr/bin/python3
# 6-square.py
# Evan Markle
# Usage:
""" This class for Square is updated to unclude a size attribute. """


class Square:
    """ This is where the size attribute is updated """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    """ This retrieves the position of the square """
    @property
    def position(self):
        return self.__position

    """ This sets the position of the square """
    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and type(value[0]) is int and type(value[1]) is int and (value[0]) >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ This calculates the area of the given square. """
    def area(self):
        return self.__size * self.__size

    """ Prints '#' to stdout """
    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
