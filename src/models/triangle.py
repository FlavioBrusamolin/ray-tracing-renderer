import math

from .shape import Shape
from .intersection import Intersection
from .shader_globals import ShaderGlobals

from utils.math import Vector2, VectorOperator, epsilon


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        vec_operator = VectorOperator()

        intersect = Intersection(False, math.inf, -1, None)

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        edge1 = vertex1.position - vertex0.position
        edge2 = vertex2.position - vertex0.position

        pvec = vec_operator.cross_product(ray.direction, edge2)
        det = vec_operator.dot_product(edge1, pvec)

        if det < epsilon:
            return intersect

        if math.fabs(det) < epsilon:
            return intersect

        inv_det = 1 / det
        tvec = ray.origin - vertex0.position
        u = vec_operator.dot_product(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return intersect

        qvec = vec_operator.cross_product(tvec, edge1)
        v = vec_operator.dot_product(ray.direction, qvec) * inv_det

        if v < 0 or u + v > 1:
            return intersect

        t = vec_operator.dot_product(edge2, qvec) * inv_det

        uv = Vector2(u, v)

        intersect.hit = True
        intersect.distance = t
        intersect.uv = uv.data

        return intersect

    def calculate_shader_globals(self, ray, intersection):
        vec_operator = VectorOperator()

        u = intersection.uv[0]
        v = intersection.uv[1]
        w = 1 - u - v

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        point = ray.point(intersection.distance)

        normal = vec_operator.normalize(
            vertex0.normal * w + vertex1.normal * u + vertex2.normal * v)

        st = vertex0.st * w + vertex1.st * u + vertex2.st * v

        tangent_u = vertex1.position - vertex0.position
        tangent_v = vertex2.position - vertex0.position

        view_direction = ray.direction * -1

        shader_globals = ShaderGlobals(
            point, normal, intersection.uv, st, tangent_u, tangent_v, view_direction, None, None, None)

        return shader_globals

    def surface_area(self):
        return -1
