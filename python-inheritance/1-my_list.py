#!/usr/bin/python3
"""
Module that defines a custom list class with sorted printing capability.
"""


class MyList(list):
    """
    A subclass of list that provides a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order without modifying it.
        """
        print(sorted(self))
