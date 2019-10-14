from .Shape import Shape


class Triangle(Shape):

    def __init__(self, vertices, bsdf):
        super().__init__(bsdf)
        self.vertices = vertices

    def intersects(self, ray):
        return ''

    def calculateShaderGlobals(self, ray, intersection):
        return ''

    def surfaceArea(self):
        return ''
