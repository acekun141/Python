"""
Lower-Upper (LU) Descomposition
"""

import numpy as np


def LUDecompose(matrix: np.array) -> [np.array, np.array]:
    """
    Parameters
    ----------
    matrix : np.array
        The root matrix
    
    Return
    ------
    L : np.array
    U : np.array
    """
    # Matrix has to be a square array so we need to check first
    rows, columns = np.shape(matrix)
    L = np.zeros((rows, columns))
    U = np.zeros((rows, columns))
    if rows != columns:
        return []
    for i in range(columns):
        for j in range(i - 1):
            sum = 0
            for k in range(j - 1):
                sum += L[i][k] * U[k][j]
            L[i][j] = (matrix[i][j] - sum) / U[j][j]
        L[i][i] = 1
        for j in range(i - 1, columns):
            sum1 = 0
            for k in range(i - 1):
                sum1 += L[i][k] * U[k][j]
            U[i][j] = matrix[i][j] - sum1
    return L, U


if __name__ == "__main__":
    matrix = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    L, U = LUDecompose(matrix)
    print(L)
    print(U)