class RenderOptions:

    def __init__(self, width, height, maximum_depth, camera_samples, light_samples, diffuse_samples, filter_width, gamma, exposure):
        self.width = width
        self.height = height
        self.maximum_depth = maximum_depth
        self.camera_samples = camera_samples
        self.light_samples = light_samples
        self.diffuse_samples = diffuse_samples
        self.filter_width = filter_width
        self.gamma = gamma
        self.exposure = exposure
