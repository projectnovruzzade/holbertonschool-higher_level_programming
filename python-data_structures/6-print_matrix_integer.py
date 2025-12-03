#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [] or matrix == [[]]:
        print("$")
    else:
        for i in range(len(matrix)):
            a = []
            for k in range(len(matrix)):
                a.append(str(matrix[i][k]))
            print(" ".join(a), end="$\n")
