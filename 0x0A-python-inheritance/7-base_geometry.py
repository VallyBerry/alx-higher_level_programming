#!/usr/bin/python3
"""
creation of basegeomaetry class
"""
class BaseGeometry:
    """A class with public instance methods and integer validators"""
    def area(self):
        """raises an exception message when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is greater than 0"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

