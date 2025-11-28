#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i+1, 10):
        if i == 8 and k == 9:
            print(f"{i}{k}")
        else:
            print(f"{i}{k}", end=", ")
