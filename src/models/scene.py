from math import inf

from .intersection import Intersection


class Scene:

    def __init__(self, shapes):
        self.shapes = shapes

    def intersects(self, ray):
        intersection = Intersection(False, inf, -1, None)

        for index, shape in enumerate(self.shapes):
            shape_intersection = shape.intersects(ray)

            if shape_intersection.distance < intersection.distance:
                intersection = shape_intersection
                intersection.index = index

        return intersection
