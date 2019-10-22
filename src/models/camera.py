import math

from utils.math import matrix4, cross_product, normalize


class Camera(object):

    def __init__(self, field_of_view, film, world_matrix):
        self.field_of_view = field_of_view
        self.film = film
        self.world_matrix = world_matrix

    def look_at(self, position, target, up):
        w = normalize(position - target)
        u = normalize(cross_product(up, w))
        v = cross_product(w, u)

        self.world_matrix = matrix4(u, v, w, position)

    def generate_ray(self, x, y, sample):
        return ''
