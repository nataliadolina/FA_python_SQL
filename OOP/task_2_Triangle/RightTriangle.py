from OOP.task_1_Vector.Vector3D import Vector3D
import math


def to_degrees(radians):
    return round(radians * 180 / math.pi, 2)


class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(a ** 2 + b ** 2)

    def corners(self):
        alpha = math.asin(self.b / self.c)
        betta = math.asin(self.b / self.c)
        return Vector3D(to_degrees(alpha), to_degrees(betta), 90)

    def P(self):
        return self.a + self.b + self.c

    def mul_procent(self, procent):
        self.a, self.b, self.c = map(lambda x: x * (1 + procent / 100), [self.a, self.b, self.c])
        return Vector3D(self.a, self.b, self.c)
