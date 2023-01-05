#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """ A class 'Square' that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate with optional size
        Args:
         size (int): Description of the parameter
         position (tuple): The position of the square, default (0, 0)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or len(position) != 2 or type(position[0]) is not int or type(position[1]) is not int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size
        Args:
         value (int): Description of the parameter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter of size"""
        return self.__positon
    
    @position.setter
    def position(self, value):
        """setter of size
        Args:
         value (tuple): The position of the square, default (0, 0)
        """
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
