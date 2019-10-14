class ShaderGlobals(object):

    def __init__(self, point, normal, uv, tangentU, tangentV, view_direction, light_direction, light_point, light_normal):
        self.point = point
        self.normal = normal
        self.uv = uv
        self.tangentU = tangentU
        self.tangentV = tangentV
        self.view_direction = view_direction
        self.light_direction = light_direction
        self.light_point = light_point
        self.light_normal = light_normal
