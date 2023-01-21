#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """public instance method that sorts the list and prints it"""
    def print_sorted(self):
        """Create a copy of the list so that the original is not modified"""
        a = self.copy()
        """Sort the list in ascending order"""
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        """Print the sorted list"""
        print(a)
