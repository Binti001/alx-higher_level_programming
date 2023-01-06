#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of instance attributes
        Args:
            width (int, optional): width of rect. Defaults to 0.
            height (int, optional): height of rect. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the rectangle
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int): width of the rectangle
        Raises:
            TypeError: when value is not an int
            ValueError: when value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int): height of the rectangle
        Raises:
            TypeError: when value is not an int
            ValueError: when value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
