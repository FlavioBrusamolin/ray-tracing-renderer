from math import sqrt, pi, cos, sin
import numpy as np


def uniform_sample_triangle(sample):
    s = sqrt(sample[0])
    u = 1.0 - s
    v = s * sample[1]

    return np.array([u, v, 1.0 - u - v])


def uniform_sample_hemisphere(sample):
    z = 1.0 - sample[0]
    s = sqrt(1.0 - z * z)
    phi = 2.0 * pi * sample[1]

    return np.array([s * cos(phi), s * sin(phi), z])
