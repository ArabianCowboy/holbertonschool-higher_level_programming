#!/usr/bin/python3
"""
Module that returns elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one set."""
    return set_1 ^ set_2
