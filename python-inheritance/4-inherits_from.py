#!/usr/bin/python3
"""
Function that return True if the object
is an istance of a class that inherited
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
