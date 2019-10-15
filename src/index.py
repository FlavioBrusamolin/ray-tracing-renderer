import numpy as np

from models.Vertex import Vertex
from models.Triangle import Triangle
from models.Scene import Scene
from models.Ray import Ray


def main():
    position_vertex1 = np.array([0, 0, 0])
    position_vertex2 = np.array([2, 0, 0])
    position_vertex3 = np.array([1, 2, 0])
    normal = np.array([0, 0, 1])
    uv = np.array([1, 1])

    first_vertex = Vertex(position_vertex1, normal, uv)
    second_vertex = Vertex(position_vertex2, normal, uv)
    third_vertex = Vertex(position_vertex3, normal, uv)

    vertices = [first_vertex, second_vertex, third_vertex]

    triangle = Triangle(vertices, 'BSDF')
    shapes = [triangle]

    scene = Scene(shapes)

    origin = np.array([1, 1, 10])
    direction = np.array([0, 0, -1])
    ray = Ray(origin, direction)

    intersection = scene.intersects(ray)

    print(intersection.hit)
    print(intersection.distance)
    print(intersection.index)


if __name__ == "__main__":
    main()
