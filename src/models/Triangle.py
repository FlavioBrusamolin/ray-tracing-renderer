import numpy as np
import math

from .Shape import Shape
from .Intersection import Intersection


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        intersect = Intersection(False, math.inf, -1)

        v0v1 = self.vertices[1].position - self.vertices[0].position
        v0v2 = self.vertices[2].position - self.vertices[0].position

        pvec = np.cross(ray.direction, v0v2)
        det = np.dot(v0v1, pvec)

        if det < np.finfo(float).eps:
            return intersect

        if abs(det) < np.finfo(float).eps:
            return intersect

        inv_det = 1 / det
        tvec = ray.origin - self.vertices[0].position
        u = np.dot(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return intersect

        qvec = np.cross(tvec, v0v1)
        v = np.dot(ray.direction, qvec) * inv_det

        if v < 0 or (u + v) > 1:
            return intersect

        t = np.dot(v0v2, qvec) * inv_det

        intersect.hit = True
        intersect.distance = t
        intersect.index = 1

        return intersect

    def calculateShaderGlobals(self, ray, intersection):
        return ''

    def surfaceArea(self):
        return ''
