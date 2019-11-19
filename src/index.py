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


def main():
    white_diffuse = BSDF(BSDFType.Diffuse, np.array([1, 1, 1]))
    red_diffuse = BSDF(BSDFType.Diffuse, np.array([1, 0, 0]))
    blue_diffuse = BSDF(BSDFType.Diffuse, np.array([0, 0, 1]))

    light = BSDF(BSDFType.Light, np.array([1, 1, 1]))

    n_top = np.array([0, -1, 0])
    n_bottom = np.array([0, 1, 0])

    triangle1 = Triangle([
        Vertex(
            np.array([0, 0, 0]),
            n_bottom,
            np.array([0, 0])
        ),
        Vertex(
            np.array([0, 0, 1]),
            n_bottom,
            np.array([1, 0])
        ),
        Vertex(
            np.array([1, 0, 1]),
            n_bottom,
            np.array([0, 1])
        )
    ], red_diffuse)

    displacement = np.array([0, 1, 0.5])

    triangle2 = Triangle([
        Vertex(
            np.array([0, 0, 0]) + displacement,
            n_top,
            np.array([0, 0])
        ),
        Vertex(
            np.array([0, 0, 1]) + displacement,
            n_top,
            np.array([1, 0])
        ),
        Vertex(
            np.array([1, 0, 1]) + displacement,
            n_top,
            np.array([0, 1])
        )
    ], light)

    scene = Scene([triangle1, triangle2], [triangle2])

    world_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    camera = Camera(pi / 2, Film(200, 200), world_matrix)
    camera.look_at(np.array([0, 50, 0]),
                   np.array([0, 0, 0]),
                   np.array([0, 0, 1]))

    render_options = RenderOptions(200, 200, 2, 2, 1, 1, 2, 2.2, 0)

    renderer = Renderer(render_options, camera, scene)
    renderer.render()


if __name__ == "__main__":
    main()
