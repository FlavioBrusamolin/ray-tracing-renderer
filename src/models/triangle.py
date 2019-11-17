from math import inf, fabs
import numpy as np

from .shape import Shape
from .intersection import Intersection
from .shader_globals import ShaderGlobals
from .utils import uniform_sample_triangle


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        intersect = Intersection(False, inf, -1, None)

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        edge1 = vertex1.position - vertex0.position
        edge2 = vertex2.position - vertex0.position

        pvec = np.cross(ray.direction, edge2)
        det = np.dot(edge1, pvec)

        if fabs(det) < np.finfo(float).eps:
            return intersect

        inv_det = 1 / det
        tvec = ray.origin - vertex0.position
        u = np.dot(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return intersect

        qvec = np.cross(tvec, edge1)
        v = np.dot(ray.direction, qvec) * inv_det

        if v < 0 or u + v > 1:
            return intersect

        t = np.dot(edge2, qvec) * inv_det

        intersect.hit = True
        intersect.distance = t
        intersect.uv = np.array([u, v])

        return intersect

    def calculate_shader_globals(self, ray, intersection):
        u = intersection.uv[0]
        v = intersection.uv[1]
        w = 1 - u - v

        vertex0 = self.vertices[0]
        vertex1 = self.vertices[1]
        vertex2 = self.vertices[2]

        point = ray.point(intersection.distance)

        _normal = vertex0.normal * w + vertex1.normal * u + vertex2.normal * v
        normal = _normal / np.linalg.norm(_normal)

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

        area = np.linalg.norm(np.cross(u, v)) / 2

        return area

    def uniform_sample(self, sample):
        v0 = self.vertices[0].position
        v1 = self.vertices[1].position
        v2 = self.vertices[2].position

        b = uniform_sample_triangle(sample)

        return v0 * b[0] + v1 * b[1] + v2 * b[2]
