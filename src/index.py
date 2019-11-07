from math import pi
import numpy as np

from models.vertex import Vertex
from models.triangle import Triangle
from models.scene import Scene
from models.film import Film
from models.camera import Camera
from models.bsdf import BSDF, BSDFType
from models.render_options import RenderOptions
from models.renderer import Renderer


def createVertex(x, y, z, s, t):
    position = np.array([x, y, z])
    normal = np.array([0, 0, 1])
    st = np.array([s, t])

    return Vertex(position, normal, st)


def main():
    vertex0 = createVertex(-0.5, -0.5, 0, 0, 0)
    vertex1 = createVertex(0.5, -0.5, 0, 1, 0)
    vertex2 = createVertex(0, 1, 0, 0, 1)

    vertices = [vertex0, vertex1, vertex2]

    color = np.array([0, 0, 0])
    bsdf = BSDF(BSDFType, color)

    triangle = Triangle(vertices, bsdf)
    shapes = [triangle]

    scene = Scene(shapes)

    film = Film(200, 200)
    world_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    camera = Camera(pi / 2, film, world_matrix)

    position = np.array([0, 0, 30])
    target = np.array([0, 0, 0])
    up = np.array([0, 1, 0])
    camera.look_at(position, target, up)

    render_options = RenderOptions(200, 200, 0, 2, 0, 0, 2, 1, 1)

    renderer = Renderer(render_options, camera, scene)
    renderer.render()


if __name__ == "__main__":
    main()
