#!/usr/bin/python3
""" defines a function that finds the attributes and methods of an object """


def lookup(obj):
    """ returns a list of attributes and methods """
    return dir(obj)
