#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """ A class 'Square' that defines a square """
    def __init__(self, size=0):
        """Instantiate with optional size
        Args:
         _size (int): Description of the parameter
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
