import math

from .intersection import Intersection


class Scene(object):

    def __init__(self, shapes):
        self.shapes = shapes

    def intersects(self, ray):
        intersection = Intersection(False, math.inf, -1)

        for shape in self.shapes:
            shape_intersection = shape.intersects(ray)

            if shape_intersection.distance < intersection.distance:
                intersection = shape_intersection

        return intersection
