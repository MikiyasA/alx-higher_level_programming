#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            print("{:d}" .format(matrix[i][j]), end='')
            if j < (len(matrix[i]) - 1):
                print(" ", end='')
        print()
