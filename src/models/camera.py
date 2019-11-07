from math import tan
import numpy as np

from .ray import Ray


class Camera:

    def __init__(self, field_of_view, film, world_matrix):
        self.field_of_view = field_of_view
        self.film = film
        self.world_matrix = world_matrix

    def look_at(self, position, target, up):
        _w = position - target
        w = _w / np.linalg.norm(_w)

        _u = np.cross(up, w)
        u = _u / np.linalg.norm(_u)

        v = np.cross(w, u)

        self.world_matrix = np.array([
            [u[0], u[1], u[2], 0],
            [v[0], v[1], v[2], 0],
            [w[0], w[1], w[2], 0],
            [position[0], position[1], position[2], 1]
        ])

    def generate_ray(self, x, y, sample):
        aspect_ratio = self.film.aspect_ratio()

        x_ndc = (x + 0.5 + sample[0]) / self.film.width
        y_ndc = (y + 0.5 + sample[1]) / self.film.height

        x_screen = 2 * x_ndc - 1
        y_screen = 1 - 2 * y_ndc

        focal_distance = tan(self.field_of_view / 2)

        x_camera = aspect_ratio * focal_distance * x_screen
        y_camera = focal_distance * y_screen
        z_camera = -1
        p_camera = np.append(np.array([x_camera, y_camera, z_camera]), 1)

        p_world = np.dot(self.world_matrix, p_camera)[:-1]

        camera_position = (self.world_matrix[3, ])[:-1]

        _direction = p_world - camera_position
        direction = _direction / np.linalg.norm(_direction)
        origin = camera_position

        return Ray(origin, direction)
