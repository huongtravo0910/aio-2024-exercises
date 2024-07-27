import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


print(compute_eigenvalues_eigenvectors(np.array([[0.9, 0.2], [0.1, 0.8]])))
