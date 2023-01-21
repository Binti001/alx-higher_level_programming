#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """public instance method that sorts the list and prints it"""
    def print_sorted(self):
        """Create a copy of the list so that the original is not modified"""
        a = self.copy()
        """Sort the list in ascending order"""
        a.sort()
        """Print the sorted list"""
        print(a)
