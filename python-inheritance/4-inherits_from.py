#!/usr/bin/python3
""" returns true if obj is inherited """


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited
    from the specified class a_class.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
