from models.vertex import Vertex
from models.triangle import Triangle
from models.scene import Scene
from models.ray import Ray
from models.bsdf import BSDF, BSDFType

from utils.math import Vector3, Vector2, VectorOperator


def createVertex(x, y, z, s, t):
    position = Vector3(x, y, z)
    normal = Vector3(0, 0, 1)
    st = Vector2(s, t)

    return Vertex(position.data, normal.data, st.data)


def main():
    vec_operator = VectorOperator()

    vertex0 = createVertex(0, 0, 0, 0, 0)
    vertex1 = createVertex(2, 0, 0, 1, 0)
    vertex2 = createVertex(1, 2, 0, 0, 1)

    vertices = [vertex0, vertex1, vertex2]

    color = Vector3(0, 0, 0)
    bsdf = BSDF(BSDFType, color.data)

    triangle = Triangle(vertices, bsdf)
    shapes = [triangle]

    scene = Scene(shapes)

    origin = Vector3(1, 1, 10)
    direction = Vector3(0, 0, -1)
    unitary_direction = vec_operator.normalize(direction.data)
    ray = Ray(origin.data, unitary_direction)

    intersection = scene.intersects(ray)

    shader_globals = triangle.calculate_shader_globals(ray, intersection)

    print(
        f'Hit: {intersection.hit}\nDistance: {intersection.distance}\nIndex: {intersection.index}\nUV: {intersection.uv}')

    print(
        f'\nPoint:{shader_globals.point}\nNormal:{shader_globals.normal}\nUV:{shader_globals.uv}\nST:{shader_globals.st}',
        f'\nTangentU:{shader_globals.tangent_u}\nTangentV:{shader_globals.tangent_v}\nView direction:{shader_globals.view_direction}')


if __name__ == "__main__":
    main()
