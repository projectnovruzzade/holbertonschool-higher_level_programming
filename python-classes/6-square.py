#!/usr/bin/python3
"""This is the module docstring."""


class Square:
    """Represents a system user."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        if type(self.__size) is not int:
            return "size must be an integer"
        else:
            return self.__size

    @size.setter
    def size(self, data):
        self.__size = data

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                a = ""
                for k in range(self.__size):
                    a += "#"
                if self.__position[1] > 0:
                    pass
                else:
                    a = " " * self.__position[0] + a
                print(a)

    @property
    def position(self):
        if type(self.__position[0] and self.__position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
