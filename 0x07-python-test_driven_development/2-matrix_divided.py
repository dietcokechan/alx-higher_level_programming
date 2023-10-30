#!/usr/bin/python3
"""divides all elements of a matrix"""

def matrix_divided(matrix, div):
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError("matric must be a matrix (list of lists) of integers/floats")
    if len(set([len(list_a) for list_a in matrix])) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
