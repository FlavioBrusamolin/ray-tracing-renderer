import numpy as np

epsilon = np.finfo(float).eps


class Vector3(object):

    def __init__(self, x, y, z):
        self.data = np.array([x, y, z])


class Vector2(object):

    def __init__(self, x, y):
        self.data = np.array([x, y])


class VectorOperator(object):

    def cross_product(self, vector1, vector2):
        return np.cross(vector1, vector2)

    def dot_product(self, vector1, vector2):
        return np.dot(vector1, vector2)
