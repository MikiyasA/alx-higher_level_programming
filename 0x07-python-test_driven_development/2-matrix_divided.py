#!/usr/bin/python3
""" The module the divide all elements of
 matrix using "def matrix_divided(matrix, div):"
"""


def matrix_divided(matrix, div):
    """ The function that divide all element
    of matrix by div
    Args:
        matrix:  list of list matrix
        div: the number used to divide all element of matrix
    """
    new_matrix = matrix.copy()

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for m_list in matrix:
        if type(m_list) is not list:
            raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")

        for e in m_list:
            if type(e) not in [int, float]:
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        for a in range(i):
            if len(matrix[i]) != len(matrix[a]):
                raise TypeError("Each row of \
the matrix must have the same size")
        new_matrix[i] = list(map(lambda x: round(x / div, 2), matrix[i]))

    return (new_matrix)
