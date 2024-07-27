import numpy as np


def compute_vector_length(v):
    len_of_vector = 0.0
    len_of_vector = np.linalg.norm(v)
    return len_of_vector


v1 = np.array([3, 4])
v2 = np.array([0, 1])

matrix1 = np.array([[1, 2], [3, -1]])
matrix2 = np.array([[1, 0], [1, 1]])

print(compute_vector_length(v1))


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


print(compute_dot_product(v1, v2))


def matrix_multi_vector(matrix, vector):
    result = vector @ matrix
    return result


print(matrix_multi_vector(v1, matrix1))


def matrix_multi_matrix(matrix1, matrix2):
    result = np.einsum('ji,ix->jx', matrix1, matrix2)
    return result


print(matrix_multi_matrix(matrix1, matrix2))


def inverse_matrix(matrix):
    det = np.linalg.det(matrix)
    if (det != 0):
        result = np.linalg.inv(matrix)
        return result
    return print('No inverse')


print(inverse_matrix(matrix1))
