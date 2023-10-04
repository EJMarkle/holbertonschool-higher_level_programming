#!/usr/bin/python3
""" returns true if objet is an intense of a class """


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
