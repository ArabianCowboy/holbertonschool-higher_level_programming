#!/usr/bin/python3
"""
Module that defines a function to return the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__
