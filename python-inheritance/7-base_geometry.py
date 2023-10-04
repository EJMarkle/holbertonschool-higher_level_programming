#!/usr/bin/python3
""" sets class BaseGeometry """


class BaseGeometry:
    """ empty class """
    def area(self):
        """ no implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if int """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
