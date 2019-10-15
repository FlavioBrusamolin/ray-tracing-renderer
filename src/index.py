from models.Vertex import Vertex
from models.Triangle import Triangle
from models.Scene import Scene
from models.Ray import Ray

from utils.math import Vector3, Vector2


def createVertex(x, y, z, s, t):
    position = Vector3(x, y, z)
    normal = Vector3(0, 0, 1)
    st = Vector2(s, t)

    return Vertex(position.data, normal.data, st.data)


def main():
    vertex0 = createVertex(0, 0, 0, 0, 0)
    vertex1 = createVertex(2, 0, 0, 1, 0)
    vertex2 = createVertex(1, 2, 0, 0, 1)

    vertices = [vertex0, vertex1, vertex2]

    triangle = Triangle(vertices, 'BSDF')
    shapes = [triangle]

    scene = Scene(shapes)

    origin = Vector3(1, 1, 10)
    direction = Vector3(0, 0, -1)
    ray = Ray(origin.data, direction.data)

    intersection = scene.intersects(ray)

    print(
        f'Hit: {intersection.hit}\nDistance: {intersection.distance}\nIndex: {intersection.index}\nUV: {intersection.uv}')

    shader_globals = triangle.calculate_shader_globals(ray, intersection)

    print(
        f'\nPoint:{shader_globals.point}\nNormal:{shader_globals.normal}\nUV:{shader_globals.uv}\nST:{shader_globals.st}\nView direction:{shader_globals.view_direction}')


if __name__ == "__main__":
    main()
