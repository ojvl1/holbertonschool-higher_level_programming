#!/usr/bin/python3
"""
    Create a class call Square
"""


class Square:
    """
        Define a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Return a the current aquare area
        """
        return self.__size ** 2
