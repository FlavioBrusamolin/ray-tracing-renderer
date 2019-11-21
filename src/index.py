from math import pi
import numpy as np
from datetime import datetime

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

    light = BSDF(BSDFType.Light, np.array([2, 2, 2]))

    size = 1.0
    left = size
    right = -size
    top = size
    bottom = -size
    front = size - 2
    back = -size - 2

    # left
    nl = np.array([-1, 0, 0])
    tl0 = Triangle([
        Vertex(
            np.array([left, bottom, back]),
            nl,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, bottom, front]),
            nl,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, top, front]),
            nl,
            np.array([0, 0])
        ),
    ], red_diffuse)

    tl1 = Triangle([
        Vertex(
            np.array([left, top, front]),
            nl,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, top, back]),
            nl,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, bottom, back]),
            nl,
            np.array([0, 0])
        ),
    ], red_diffuse)

    # right
    nr = np.array([1, 0, 0])
    tr0 = Triangle([
        Vertex(
            np.array([right, bottom, front]),
            nr,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, bottom, back]),
            nr,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top, back]),
            nr,
            np.array([0, 0])
        ),
    ], blue_diffuse)

    tr1 = Triangle([
        Vertex(
            np.array([right, top, back]),
            nr,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top, front]),
            nr,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, bottom, front]),
            nr,
            np.array([0, 0])
        ),
    ], blue_diffuse)

    # top
    nt = np.array([0, -1, 0])
    tt0 = Triangle([
        Vertex(
            np.array([left, top, front]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top, front]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top, back]),
            nt,
            np.array([0, 0])
        ),
    ], white_diffuse)

    tt1 = Triangle([
        Vertex(
            np.array([right, top, back]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, top, back]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, top, front]),
            nt,
            np.array([0, 0])
        ),
    ], white_diffuse)

    # bottom
    nb_ = np.array([0, 1, 0])
    tb_0 = Triangle([
        Vertex(
            np.array([left, bottom, front]),
            nb_,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, bottom, front]),
            nb_,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, bottom, back]),
            nb_,
            np.array([0, 0])
        ),
    ], white_diffuse)

    tb_1 = Triangle([
        Vertex(
            np.array([right, bottom, back]),
            nb_,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, bottom, back]),
            nb_,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, bottom, front]),
            nb_,
            np.array([0, 0])
        ),
    ], white_diffuse)

    # back
    nb = np.array([0, 0, 1])
    tb0 = Triangle([
        Vertex(
            np.array([left, bottom, back]),
            nb,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, bottom, back]),
            nb,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top, back]),
            nb,
            np.array([0, 0])
        ),
    ], white_diffuse)

    tb1 = Triangle([
        Vertex(
            np.array([right, top, back]),
            nb,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, top, back]),
            nb,
            np.array([0, 0])
        ),
        Vertex(
            np.array([left, bottom, back]),
            nb,
            np.array([0, 0])
        ),
    ], white_diffuse)

    # light
    l0 = Triangle([
        Vertex(
            np.array([left, top - 0.01, back]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([right, top - 0.01, back]),
            nt,
            np.array([0, 0])
        ),
        Vertex(
            np.array([0, top - 0.01, front]),
            nt,
            np.array([0, 0])
        ),
    ], light)

    scene = Scene([tl0, tl1, tr0, tr1, tt0, tt1,
                   tb_0, tb_1, tb0, tb1, l0], [l0])

    world_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    camera = Camera(pi / 2, Film(400, 400), world_matrix)
    camera.look_at(np.array([0, 0, 10]),
                   np.array([0, 0, 0]),
                   np.array([-1, 0, 0]))

    render_options = RenderOptions(400, 400, 2, 2, 1, 1, 2, 2.2, 0)

    renderer = Renderer(render_options, camera, scene)
    renderer.render()

    print('Rendering completed.')
    print(datetime.now())


if __name__ == "__main__":
    main()
