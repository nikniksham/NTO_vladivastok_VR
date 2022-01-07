"""
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
"""

"""
[0.0, -0.0, 1.0, -1.0, [14, 16, 3, 1]]
(0.0, 0.0, 0.0)
[(0.418099, -0.418099, 1.0), (0.418099, 0.418099, 1.0), (-0.418099, 0.418099, 1.0), (-0.418099, -0.418099, 1.0)]
"""


def vec_multiplication(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]


def scalar(ver1, ver2):
    return ver1[0] * ver2[0] + ver1[1] * ver2[1] + ver1[2] * ver2[2]


def get_len(ver):
    return (scalar(ver, ver))**0.5


def make_ed(ver):
    le = get_len(ver)
    if le != 0:
        return ver[0] / le, ver[1] / le, ver[2] / le
    return [0, 0, 0]


def subtr(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]


def plosk_by_point_and_norm(m, n, p):
    return n[0]*(p[0] - m[0]) + n[1]*(p[1] - m[1]) + n[2]*(p[2] - m[2])

r = 0.3
edge = [0.0, -0.0, 1.0, -1.0, [14, 16, 3, 1]]
edge_points = [(0.418099, -0.418099, 1.0), (0.418099, 0.418099, 1.0), (-0.418099, 0.418099, 1.0), (-0.418099, -0.418099, 1.0)]
p1 = (0.0, 0.0, 0.0)
v1 = (0.7071067811865475, 0.0, 0.7071067811865475)

need = False
p2 = edge_points[-1]
v2 = make_ed(subtr(p2, edge_points[0]))
norm = make_ed(vec_multiplication(v1, v2))
print(v2, norm, v1)
print(plosk_by_point_and_norm(p1, norm, p2))

for i in range(len(edge_points) - 1):
    p2 = edge_points[i]
    v2 = make_ed(subtr(edge_points[i], edge_points[i + 1]))
    norm = make_ed(vec_multiplication(v1, v2))
    print(plosk_by_point_and_norm(p1, norm, p2))
    if abs(plosk_by_point_and_norm(p1, norm, p2)) < r:
        print(abs(plosk_by_point_and_norm(p1, norm, p2)))
        print(123)
        print(edge_points[i], edge_points[i + 1])
        need = True
        break
"""
a, b, c, d = edge[:4]
edge_points = [vertices[i] for i in edge[4]]
# print(point)
if point:
    p1 = (x0, y0, z0)
    v1 = (u, v, w)
    
    # TODO: Пофиксить плохое вычисление краёв цилиндра в шаре

    # Поправить расчёт, он должен вычисляться с проекцией точки и всеми рёбрами

    need = False
    p2 = edge_points[-1]
    v2 = make_ed(subtr(edge_points[-1], edge_points[0]))
    norm = vec_multiplication(v1, v2)
    if abs(plosk_by_point_and_norm(p1, norm, p2)) < r:
        need = True

    if not need:
        for i in range(len(edge_points) - 1):
            p2 = edge_points[i]
            v2 = make_ed(subtr(edge_points[i], edge_points[i + 1]))
            norm = vec_multiplication(v1, v2)
            if abs(plosk_by_point_and_norm(p1, norm, p2)) < r:
                # print(abs(plosk_by_point_and_norm(p1, norm, p2)))
                # print(123)
                # print(edge_points[i], edge_points[i + 1])
                need = True
                break"""