vec_abs = lambda vec3: sum(map(lambda x: x**2, vec3))**0.5
vec_multiplication = lambda a, b: [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
plosk_by_point_and_norm = lambda m, n, p: n[0]*(p[0] - m[0]) + n[1]*(p[1] - m[1]) + n[2]*(p[2] - m[2])


def make_ed(ver):
    le = vec_abs(ver)
    return ver[0] / le, ver[1] / le, ver[2] / le


# прямая 1
p1 = ( 1, 3, 0)  # точка прямой
v1 = ( 0, 1, 0)  # вектор направления
# прямая 2
p2 = (-1, 0, 0)  # точка прямой
v2 = ( 0, 0, 1)  # вектор направления


norm = vec_multiplication(make_ed(v1), make_ed(v2))
print(abs(plosk_by_point_and_norm(p1, norm,  p2)))