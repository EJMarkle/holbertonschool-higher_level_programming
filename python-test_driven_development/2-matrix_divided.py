#!/usr/bin/python3
"""
Divides the elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Args:
        matrix: containing ints and floats
        div: what matrix will be divided by

    Raises:
        TypeError: if matrix is not list of ints or floats
        ZeroDivisionError: if div = 0

    Returns:
        new divided matrix rounded to 2 decimal places
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []

    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        divided_matrix.append(new_row)

    return divided_matrix
