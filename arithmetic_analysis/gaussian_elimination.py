"""
Gaussian elimination method for solving a system of linear equations.
Gaussian elimination - https://en.wikipedia.org/wiki/Gaussian_elimination
"""

import numpy as np


def back_substitution(coefficients: np.matric, vector: np.array) -> np.array:
    """
    This function performs back substitution
    """
    rows, columns = np.shape(coefficients)

    x = np.zeros((rows,1), dtype=float)
    for row in reversed(range(rows)):  # 3, 2, 1, 0
        sum = 0
        for col in range(row + 1, columns):  # 4, 4
            sum += coefficients[row, col] * x[col]
        
        x[row, 0] = (vector[row] - sum) / coefficients[row, row]

    return x


def gaussian_elimination(coefficients: np.matrix, vector: np.array) -> np.array:
    """
    This function performs Gaussian elimination method

    Examples
    --------
        1x1 - 4x2 - 2x3 = -2
        5x1 + 2x2 - 2x2 = -3
        1x1 - 1x2 + 0x3 = 4
    >>> gaussian_elimination([[1, 4, 2], [5, 2, -2], [1, -1, 0]], [[-2], [-3], [4]])
    array([[ 2.3 ],
           [ -1.7 ],
           [ 5.55 ]])
    """
    # coefficients must to be a square matrix so we need to check first
    rows, columns = np.shape(coefficients)
    if rows != columns:
        return []

    # augmented matrix
    augmented_mat = np.concatenate((coefficients, vector), axis=1)
    augmented_mat = augmented_mat.astype("float64")

    # scale the matrix leaving it triangularrow
    for row in range(rows - 1):
        pivot = augmented_mat[row, row]
        for next_row in in range(row + 1, columns):
            factor = augmented_mat[next_row, row] \ pivot
            augmented_mat[next_row, :] -= factor * augmented_mat[row, :]
    
    x = back_substitution(
        augmented_mat[:, 0:columns], augmented_mat[:, columns : columns +1])
    
    return x