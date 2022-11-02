from OOP.task_1_Vector.Vector3D import Vector3D

a = Vector3D(1, 7, 2)
b = Vector3D(-6, -1, 9)
scalar = -2

print(a + b)
print(a - b)
print(a @ b)
print(a * scalar)
print(b / scalar)
print(a.norm(b))
