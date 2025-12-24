#!/usr/bin/python3
"""
this is global enviroment
"""


def inherits_from(obj, a_class):
    """
    this is function enviroment
    """
    return type(obj) is not a_class
