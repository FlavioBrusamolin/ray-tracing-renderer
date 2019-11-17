from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, bsdf):
        self.bsdf = bsdf

    @abstractmethod
    def intersects(self, ray):
        pass

    @abstractmethod
    def calculate_shader_globals(self, ray, intersection):
        pass

    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def uniform_sample(self):
        pass
