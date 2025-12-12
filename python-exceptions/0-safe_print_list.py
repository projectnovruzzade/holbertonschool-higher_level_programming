#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    spc = x - 1 if len(my_list) > x else len(my_list) - 1
    try:
        for i in range(x):
            if i == spc:
                print(my_list[i], end="\n")
            else:
                print(my_list[i], end="")
            c += 1
    except Exception as e:
        pass
    return c
