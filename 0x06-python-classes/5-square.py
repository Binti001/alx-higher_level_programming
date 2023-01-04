#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """ A class 'Square' that defines a square """
    def __init__(self, size=0):
        """Instantiate with optional size
        Args:
         _size (int): Description of the parameter
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
