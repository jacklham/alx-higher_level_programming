#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    first method using map and lambda

    lamb = lambda x: x**2
    return list(map(lambda row: list(map(lamb, row)), matrix))

    Second method below using list comprehension
    """
    return [[x**2 for x in row] for row in matrix]
