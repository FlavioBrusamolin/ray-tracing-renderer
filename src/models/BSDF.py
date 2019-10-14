from enum import Enum


class BSDFType(Enum):
    Light = 0
    Diffuse = 1
    Specular = 2
    Any = 3


class BSDF(object):

    def __init__(self, type, color):
        self.type = type
        self.color = color
