#!/usr/bin/python3
import sys

if __name__ == "__main__":
    all_numbers = sys.argv
    result = 0
    for i in range(1, len(all_numbers)):
        result = result + int(all_numbers[i])
    print(result)
