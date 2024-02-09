#!/usr/bin/python3
"""Create a class"""


class BaseGeometry:
    """add public method integer_validator"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be gerater than 0".format(name))
