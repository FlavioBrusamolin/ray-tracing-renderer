import numpy as np

EPSILON = np.finfo(float).eps


def vector2(x, y):
    return np.array([x, y], np.float64)


def vector3(x, y, z):
    return np.array([x, y, z], np.float64)


def matrix4(u, v, w, p):
    return np.array([
        [u[0], u[1], u[2], 0],
        [v[0], v[1], v[2], 0],
        [w[0], w[1], w[2], 0],
        [p[0], p[1], p[2], 1]
    ])


def cross_product(vector1, vector2):
    return np.cross(vector1, vector2)


def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)


def absolute(vector):
    return np.linalg.norm(vector)


def normalize(vector):
    return vector / absolute(vector)


def append(vector1, vector2):
    return np.append(vector1, vector2)
