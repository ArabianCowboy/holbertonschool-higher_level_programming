#!/usr/bin/python3
"""BaseGeometry module.
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation."""
    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): name of the parameter.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
