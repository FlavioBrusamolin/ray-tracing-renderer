import math
from random import random

from PIL import Image

import numpy as np

from utils.math import vector3, vector2


class Renderer:

    def __init__(self, options, camera, scene):
        self.options = options
        self.camera = camera
        self.scene = scene

    def compute_direct_illumination(self, bsdf, shader_globals):
        pass

    def compute_indirect_illumination(self, bsdf, shader_globals, depth):
        pass

    def trace(self, ray, depth):
        intersection = self.scene.intersects(ray)

        if intersection.hit:
            return vector3(1, 1, 1)

        return vector3(0, 0, 0)

    def render(self):
        camera_samples = self.options.camera_samples
        filter_width = self.options.filter_width

        image = np.zeros(
            (self.camera.film.width, self.camera.film.height, 3), np.uint8)

        for i in range(self.camera.film.width):
            for j in range(self.camera.film.height):
                samples = self.stratified_samples(camera_samples)

                color = vector3(0, 0, 0)
                total_weight = 0.0

                for k in range(camera_samples):
                    sample = (samples[k] - vector2(0.5, 0.5)) * filter_width
                    ray = self.camera.generate_ray(i, j, sample)
                    weight = self.gaussian_2d(sample, filter_width)

                    color += self.trace(ray, 0) * weight
                    total_weight += weight

                color /= total_weight

                image[i, j] = (
                    self.saturate(
                        self.gamma(
                            self.exposure(
                                color,
                                self.options.exposure),
                            self.options.gamma)) * 255).astype(np.uint8)

        im = Image.fromarray(image)
        im.show()

    def stratified_samples(self, samples):
        size = math.ceil(math.sqrt(samples))

        points = []

        for i in range(size):
            for j in range(size):
                offset = vector2(i, j)
                points.append((offset + vector2(random(), random())) / size)

        return points

    def gaussian_2d(self, sample, filter_width):
        r = filter_width / 2

        k_x = max(math.exp(- sample[0] * sample[0]) - math.exp(- r * r), 0)
        k_y = max(math.exp(- sample[1] * sample[1]) - math.exp(- r * r), 0)

        return k_x * k_y

    def gamma(self, color, value):
        inverse_gamma = 1 / value

        return vector3(pow(color[0], inverse_gamma),
                       pow(color[1], inverse_gamma),
                       pow(color[2], inverse_gamma))

    def exposure(self, color, value):
        power = pow(2, value)

        return vector3(color[0] * power, color[1] * power, color[2] * power)

    def saturate(self, color):
        def truncate(value):
            if value <= 0:
                return 0
            elif value >= 1:
                return 1
            else:
                return value

        for i in range(color.shape[0]):
            color[i] = truncate(color[i])

        return color
