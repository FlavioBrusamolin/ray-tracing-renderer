class ShaderGlobals(object):

    def __init__(self, point, normal, uv, st, tangent_u, tangent_v, view_direction, light_direction, light_point, light_normal):
        self.point = point
        self.normal = normal
        self.uv = uv
        self.st = st
        self.tangent_u = tangent_u
        self.tangent_v = tangent_v
        self.view_direction = view_direction
        self.light_direction = light_direction
        self.light_point = light_point
        self.light_normal = light_normal
