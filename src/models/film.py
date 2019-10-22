class Film(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def aspect_ratio(self):
        return self.width / self.height
