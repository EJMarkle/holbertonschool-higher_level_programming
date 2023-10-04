#!/usr/bin/python3
""" defines a class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a class that inherits BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", seld.__width)
        self.integer_validator("height", self.__height)
