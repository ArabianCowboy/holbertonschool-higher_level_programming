#!/usr/bin/python3
"""
Module that defines a function to check class inheritance or matching.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a class inherited from it.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a_class or a subclass, otherwise False
    """
    return isinstance(obj, a_class)
