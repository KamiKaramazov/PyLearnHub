import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        norm = self.length()
        if norm != 0:
            return self / norm
        else:
            return self

    def rotate(self, angle):
        rad = math.radians(angle)
        return Vector(self.x * math.cos(rad) - self.y * math.sin(rad), self.x * math.sin(rad) + self.y * math.cos(rad))