#!/usr/bin/python3
"""
this is global enviroment
"""


def read_file(filename=""):
    """
    this is internal enviroment
    """
    with open("my_file_0.txt", "r", encoding="utf-8") as file:
        data = file.read()
        print(data)
