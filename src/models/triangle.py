import math

from .shape import Shape
from .intersection import Intersection
from .shader_globals import ShaderGlobals

from utils.math import EPSILON, vector2, cross_product, dot_product, absolute, normalize


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        intersect = Intersection(False, math.inf, -1, None)

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        edge1 = vertex1.position - vertex0.position
        edge2 = vertex2.position - vertex0.position

        pvec = cross_product(ray.direction, edge2)
        det = dot_product(edge1, pvec)

        if math.fabs(det) < EPSILON:
            return intersect

        inv_det = 1 / det
        tvec = ray.origin - vertex0.position
        u = dot_product(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return intersect

        qvec = cross_product(tvec, edge1)
        v = dot_product(ray.direction, qvec) * inv_det

        if v < 0 or u + v > 1:
            return intersect

        t = dot_product(edge2, qvec) * inv_det

        intersect.hit = True
        intersect.distance = t
        intersect.uv = vector2(u, v)

        return intersect

    def calculate_shader_globals(self, ray, intersection):
        u = intersection.uv[0]
        v = intersection.uv[1]
        w = 1 - u - v

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        point = ray.point(intersection.distance)

        normal = normalize(
            vertex0.normal * w + vertex1.normal * u + vertex2.normal * v)

        st = vertex0.st * w + vertex1.st * u + vertex2.st * v

        tangent_u = vertex1.position - vertex0.position
        tangent_v = vertex2.position - vertex0.position

        view_direction = ray.direction * -1

        shader_globals = ShaderGlobals(
            point, normal, intersection.uv, st, tangent_u, tangent_v, view_direction, None, None, None)

        return shader_globals

    def surface_area(self):
        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        u = vertex1.position - vertex0.position
        v = vertex2.position - vertex0.position

        area = absolute(cross_product(u, v)) / 2

        return area
