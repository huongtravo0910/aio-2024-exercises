import numpy as np
from numpy import dot
from numpy.linalg import norm


def compute_cosine(v1, v2):
    cos_sim = dot(v1, v2)/(norm(v1)*norm(v2))
    return cos_sim


print(compute_cosine(np.array([1, 2]), np.array([2, 4])))
