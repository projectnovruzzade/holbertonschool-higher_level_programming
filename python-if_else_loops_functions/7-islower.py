#!/usr/bin/python3
islower = __import__('7-islower').islower


def islower(letter):
    if 97 <= ord(letter) <= 122 or 0 <= ord(letter) < 10:
        return "lower"
    else:
        return "upper"
