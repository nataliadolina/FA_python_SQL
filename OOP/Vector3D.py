import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(other.x + self.x, other.y + self.y, other.z + self.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        return other.x * self.x + other.y * self.y + other.z * self.z

    def __truediv__(self, other):
        """

        :type other: float
        :return: Vector3D
        """
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def norm(self, other=None):
        """

        :type other: Vector3D
        :return: float
        """
        if not other:
            other = Vector3D(0, 0, 0)
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2) + math.pow(self.z - other.z, 2))

    def __matmul__(self, other):
        """

        :type other: Vector3D
        :return: Vector3D
        """
        sin = math.sqrt(1 - math.pow((self * other) / self.norm(other), 2))

        return self.norm() * other.norm() * sin
