from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, bsdf):
        self.bsdf = bsdf

    @abstractmethod
    def intersects(self, ray):
        pass

    @abstractmethod
    def calculateShaderGlobals(self, ray, intersection):
        pass

    @abstractmethod
    def surfaceArea(self):
        pass
