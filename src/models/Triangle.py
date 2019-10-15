import math

from .shape import Shape
from .intersection import Intersection

from utils.math import VectorOperator, epsilon


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        vector_operator = VectorOperator()

        intersect = Intersection(False, math.inf, -1)

        v0v1 = self.vertices[1].position - self.vertices[0].position
        v0v2 = self.vertices[2].position - self.vertices[0].position

        pvec = vector_operator.cross_product(ray.direction, v0v2)
        det = vector_operator.dot_product(v0v1, pvec)

        if det < epsilon:
            return intersect

        if math.fabs(det) < epsilon:
            return intersect

        inv_det = 1 / det
        tvec = ray.origin - self.vertices[0].position
        u = vector_operator.dot_product(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return intersect

        qvec = vector_operator.cross_product(tvec, v0v1)
        v = vector_operator.dot_product(ray.direction, qvec) * inv_det

        if v < 0 or (u + v) > 1:
            return intersect

        t = vector_operator.dot_product(v0v2, qvec) * inv_det

        intersect.hit = True
        intersect.distance = t
        intersect.index = 1

        return intersect

    def calculateShaderGlobals(self, ray, intersection):
        return ''

    def surfaceArea(self):
        return ''
