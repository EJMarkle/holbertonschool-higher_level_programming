#!/usr/bin/python3
""" defines a function to check if an object is in a class """


def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class."""
    return type(obj) is a_class
