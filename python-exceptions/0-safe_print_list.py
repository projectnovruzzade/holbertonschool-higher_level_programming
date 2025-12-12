#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        return 0
    c = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            c += 1
            if c == x:
                print("", end="\n")
    except Exception:
        print("", end="\n")
    return c
