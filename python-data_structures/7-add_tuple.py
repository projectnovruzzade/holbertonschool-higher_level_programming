#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = ()
    c = 0
    if len(tuple_b) == 0:
        tuple_b = tuple_b + (0, 0, )
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0, )
    for a, b in zip(tuple_a, tuple_b):
        t = t + (a + b,)
        c += 1
        if c == 2:
            break
    return t
