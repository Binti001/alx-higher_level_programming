#!/usr/bin/python3
"""a function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """Create an empty list"""
    attr_meth = []
    """Loop through the object"""
    for i in dir(obj):
        """Append the item to the list"""
        attr_meth.append(i)
    """return the list"""
    return attr_meth
