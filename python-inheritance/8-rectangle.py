#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
this is global enviroment
"""


class Rectangle(BaseGeometry):
    """
        this is local enviroment
    """
    def __init__(self, width, height):
        """
            this is local enviroment
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
