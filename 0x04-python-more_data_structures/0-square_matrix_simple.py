#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions
    new_matrix = [row[:] for row in matrix]
    
    # Iterate over each element in the matrix
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            # Square each element
            new_matrix[i][j] = new_matrix[i][j] ** 2
            
    return new_matrix
