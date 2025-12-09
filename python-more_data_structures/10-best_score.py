#!/usr/bin/python3
def best_score(a_dictionary):
    maxNum = 0
    maxMan = ""
    if a_dictionary is None:
        return None
    for (k, v) in a_dictionary.items():
        if v > maxNum:
            maxNum = v
            maxMan = k
    return maxMan
