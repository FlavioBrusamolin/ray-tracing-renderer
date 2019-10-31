import math

from models.vertex import Vertex
from models.triangle import Triangle
from models.scene import Scene
from models.film import Film
from models.camera import Camera
from models.bsdf import BSDF, BSDFType
from models.render_options import RenderOptions
from models.renderer import Renderer

from utils.math import vector2, vector3, matrix4


def createVertex(x, y, z, s, t):
    position = vector3(x, y, z)
    normal = vector3(0, 0, 1)
    st = vector2(s, t)

    return Vertex(position, normal, st)


def main():
    vertex0 = createVertex(-0.5, -0.5, 0, 0, 0)
    vertex1 = createVertex(0.5, -0.5, 0, 1, 0)
    vertex2 = createVertex(0, 1, 0, 0, 1)

    vertices = [vertex0, vertex1, vertex2]

    color = vector3(0, 0, 0)
    bsdf = BSDF(BSDFType, color)

    triangle = Triangle(vertices, bsdf)
    shapes = [triangle]

    scene = Scene(shapes)

    film = Film(200, 200)
    world_matrix = matrix4(vector3(1, 0, 0), vector3(0, 1, 0),
                           vector3(0, 0, 1), vector3(0, 0, 0))

    camera = Camera(math.pi / 2, film, world_matrix)

    position = vector3(0, 0, 30)
    target = vector3(0, 0, 0)
    up = vector3(0, 1, 0)
    camera.look_at(position, target, up)

    render_options = RenderOptions(200, 200, 0, 5, 0, 0, 2, 1, 1)

    renderer = Renderer(render_options, camera, scene)
    renderer.render()


if __name__ == "__main__":
    main()
