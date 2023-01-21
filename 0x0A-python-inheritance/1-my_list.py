#!/usr/bin/python3
"""class MyList that inherits from list"""

class MyList(list):
    """class that inherits from the built-in list class"""
    def print_sorted(self):
        """public instance method that sorts the list and prints it"""
        a = self.copy()
        """Create a copy of the list so that the original is not modified"""
        for i in range(len(a) - 1):
            """Sort the list in ascending order"""
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        """Print the sorted list"""
        print(a)
