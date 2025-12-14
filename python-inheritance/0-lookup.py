#!/usr/bin/python3
"""
Module that defines a function to list attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        A list of attribute and method names
    """
    return dir(obj)
