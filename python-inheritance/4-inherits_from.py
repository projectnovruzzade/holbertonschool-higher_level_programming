#!/usr/bin/python3
"""
this is global enviroment
"""


def inherits_from(obj, a_class):
    """
    this is function enviroment
    """
    return type(obj) and isinstance(obj,a_class) is not a_class
