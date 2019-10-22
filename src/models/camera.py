import math

from .ray import Ray

from utils.math import vector3, matrix4, cross_product, dot_product, normalize, append


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
        aspect_ratio = self.film.aspect_ratio()

        x_ndc = (x + 0.5) / self.film.width
        y_ndc = (y + 0.5) / self.film.height

        x_screen = 2 * x_ndc - 1
        y_screen = 1 - 2 * y_ndc

        focal_distance = math.tan(self.field_of_view / 2)

        x_camera = aspect_ratio * focal_distance * x_screen
        y_camera = focal_distance * y_screen
        z_camera = -1
        p_camera = append(vector3(x_camera, y_camera, z_camera), 1)

        p_world = dot_product(self.world_matrix, p_camera)[:-1]

        camera_position = (self.world_matrix[3, ])[:-1]

        direction = normalize(p_world - camera_position)
        origin = camera_position

        return Ray(origin, direction)
