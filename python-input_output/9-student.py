#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        that exist in the instance are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for a in attrs:
                if hasattr(self, a):
                    result[a] = getattr(self, a)
            return result
        return self.__dict__
