#!/usr/bin/python3
islower = __import__('7-islower').islower


def islower(c):
    if 97 <= ord(c) <= 122 or 0 <= ord(c) < 10:
        return "{} is lower".format(c)
    else:
        return "{} is upper".format(c)
