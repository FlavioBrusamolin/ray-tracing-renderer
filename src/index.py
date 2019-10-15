from models.vertex import Vertex
from models.triangle import Triangle
from models.scene import Scene
from models.ray import Ray

from utils.math import Vector3, Vector2


def createVertex(x, y, z, u, v):
    position = Vector3(x, y, z)
    normal = Vector3(0, 0, 1)
    uv = Vector2(u, v)

    return Vertex(position.data, normal.data, uv.data)


def main():
    vertex1 = createVertex(0, 0, 0, 0, 0)
    vertex2 = createVertex(2, 0, 0, 1, 0)
    vertex3 = createVertex(1, 2, 0, 0, 1)

    vertices = [vertex1, vertex2, vertex3]

    triangle = Triangle(vertices, 'BSDF')
    shapes = [triangle]

    scene = Scene(shapes)

    origin = Vector3(1, 1, 10)
    direction = Vector3(0, 0, -1)
    ray = Ray(origin.data, direction.data)

    intersection = scene.intersects(ray)

    print(
        f'Hit: {intersection.hit}\nDistance: {intersection.distance}\nIndex: {intersection.index}')


if __name__ == "__main__":
    main()
