class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def point(self, distance):
        return self.origin + self.direction * distance
