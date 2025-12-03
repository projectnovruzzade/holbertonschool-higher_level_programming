#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [] or matrix == [[]]:
        print("$")
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i < len(row) - 1:
                    print("{}".format(num), end=" ")
                else:
                    print("{}".format(num), end="")
            print("$")
