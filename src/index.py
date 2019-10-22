import math

from models.vertex import Vertex
from models.triangle import Triangle
from models.scene import Scene
from models.film import Film
from models.camera import Camera
from models.bsdf import BSDF, BSDFType

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

    film = Film(1920, 1080)
    world_matrix = matrix4(vector3(1, 0, 0), vector3(0, 1, 0),
                           vector3(0, 0, 1), vector3(0, 0, 0))

    camera = Camera(math.pi / 4, film, world_matrix)

    position = vector3(0, 0, 30)
    target = vector3(0, 0, 0)
    up = vector3(0, 1, 0)
    camera.look_at(position, target, up)

    ray = camera.generate_ray(960, 540, vector2(0, 0))

    intersection = scene.intersects(ray)

    print(f'Hit: {intersection.hit}\nDistance: {intersection.distance}\nIndex: {intersection.index}\nUV: {intersection.uv}')

    if intersection.hit:
        shader_globals = triangle.calculate_shader_globals(ray, intersection)

        print(
            f'\nPoint:{shader_globals.point}\nNormal:{shader_globals.normal}\nUV:{shader_globals.uv}\nST:{shader_globals.st}',
            f'\nTangentU:{shader_globals.tangent_u}\nTangentV:{shader_globals.tangent_v}\nView direction:{shader_globals.view_direction}'
        )


if __name__ == "__main__":
    main()
