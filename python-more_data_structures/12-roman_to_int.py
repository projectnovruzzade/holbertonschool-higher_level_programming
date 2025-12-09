#!/usr/bin/python3
def roman_to_int(roman_string):
    example = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(roman_string) == 1:
        return example[roman_string]
    total = example[roman_string[0]]
    temp = example[roman_string[0]]
    for i in range(1, len(roman_string)):
        if temp - example[roman_string[i]] >= 0:
            total = total + example[roman_string[i]]
            temp = example[roman_string[i]]
        else:
            total = example[roman_string[i]] - total
    return total
