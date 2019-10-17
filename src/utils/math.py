import numpy as np

EPSILON = np.finfo(float).eps


def vector2(x, y):
    return np.array([x, y])


def vector3(x, y, z):
    return np.array([x, y, z])


def cross_product(vector1, vector2):
    return np.cross(vector1, vector2)


def dot_product(vector1, vector2):
    return np.dot(vector1, vector2)


def absolute(vector):
    return np.linalg.norm(vector)


def normalize(vector):
    return vector / absolute(vector)
