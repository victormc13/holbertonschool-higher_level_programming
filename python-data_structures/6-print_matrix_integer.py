#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        return [[]]

    for row in matrix:
        for element in range(len(row)):
            if (element == len(row) - 1):
                print("{}".format(row[element]))
            else:
                print("{}".format(row[element]), end=" ")
