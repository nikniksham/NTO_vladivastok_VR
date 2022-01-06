from time import time
from math import tan, asin
st = time()


def vec_abs(vec3):
    return sum(map(lambda x: x**2, vec3))**0.5


def plosk_by_point_and_norm(m, n, p):
    return n[0]*(p[0] - m[0]) + n[1]*(p[1] - m[1]) + n[2]*(p[2] - m[2])


def vec_multiplication_by_const(a, b):
    return [a[0]*b, a[1]*b, a[2]*b]


def vec_addition(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def vec_multiplication(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]


def get_d(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5


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


def get_dist_between_lines(vec, p1, pl1, pl2):
    u, v, w = vec
    x0, y0, z0 = p1
    xl, yl, zl = pl2
    ul, vl, wl = subtr(pl1, pl2)


def get_dist_to_plane(point, edge):
    return (edge[0] * point[0] + edge[1] * point[1] + edge[2] * point[2] + edge[3]) / (edge[0]**2+edge[1]**2+edge[2]**2)**0.5


def get_point_crossing(point, m0, edge):
    u, v, w = point
    vec_pl = [edge[0], edge[1], edge[2]]
    scl = scalar([u, v, w], vec_pl)
    # print(scl)
    if scl != 0:
        # xp, yp, zp = d + m0[0], d + m0[1], d + m0[2]
        t = edge[0] * u + edge[1] * v + edge[2] * w
        oth = edge[0] * m0[0] + edge[1] * m0[1] + edge[2] * m0[2] + edge[3]
        # print(t, oth)
        t = -oth / t
        # print(t)
        xp, yp, zp = t * u + m0[0], t * v + m0[1], t * w + m0[2]
        # print(xp, yp, zp)
        return [round(xp, 7), round(yp, 7), round(zp, 7)]
    return None


def calculate(file):
    menshe = False
    count_vertices = int(file.readline())
    vertices = []
    for _ in range(count_vertices):
        vertices.append(tuple(map(float, file.readline().split())))
    file.readline()
    count_edge = int(file.readline())
    edges = []
    for _ in range(count_edge):
        arr = list(map(int, file.readline().split()))[1:]
        p0 = vertices[arr[0]]
        p1 = vertices[arr[1]]
        p2 = (0, 0, 0)
        for ver_id in arr[2:]:
            p2 = vertices[ver_id]
            # print(p2)
            if round(get_d(p0, p2) + get_d(p1, p2) - get_d(p0, p1), 6) * round(
                    get_d(p0, p2) + get_d(p0, p1) - get_d(p1, p2), 6) * round(
                get_d(p0, p1) + get_d(p1, p2) - get_d(p0, p2), 6) != 0:
                # p2 = subtr(vertices[ver_id], p0)
                break
        # print(p0, p1, p2,)
        ps = [p0, p1, p2]
        p1 = subtr(p0, p1)
        p2 = subtr(p0, p2)
        a, b, c = (p1[1] * p2[2] - p1[2] * p2[1]), -(p1[0] * p2[2] - p1[2] * p2[0]), (p1[0] * p2[1] - p1[1] * p2[0])
        a, b, c = make_ed((a, b, c))
        d = -p0[0] * a - p0[1] * b - p0[2] * c
        edges.append([a, b, c, d, arr])

    # ax + by + cz + d = 0
    # (x - x0)**2/r**2 + (y - y0)**2/r**2 + (z - z0)**2/r**2 - 1 = 0
    # print(edges)
    file.readline()
    x0, y0, z0 = map(float, file.readline().split())
    u, v, w = map(float, file.readline().split())
    r = float(file.readline().split()[0])
    d = (u ** 2 + v ** 2 + w ** 2) ** 0.5
    m0 = [u, v, w]
    u2, v2, w2 = u, v, w
    u, v, w = u / d, v / d, w / d
    # print(u, v, w)

    points = []
    for edge in edges:
        points.append(get_point_crossing([u, v, w], m0, edge))

    projections = []
    for edge, point in zip(edges, points):
        a, b, c, d = edge[:4]
        if point:
            otcl = a * x0 + b * y0 + c * z0 + d
            # print(subtr([-a * otcl + x0, -b * otcl + y0, -c * otcl + z0], point), point)
            projections.append((make_ed(subtr([-a * otcl + x0, -b * otcl + y0, -c * otcl + z0], point)), point))
        else:
            projections.append(None)

    ps = []
    ts = []
    for i in range(len(points)):
        if points[i]:
            x, y, z = points[i]
            if u != 0:
                t = (x - x0) / u
            elif v != 0:
                t = (y - y0) / v
            else:
                t = (z - z0) / w
            # print(t)
            # print(points[i], i)
            ts.append(t)
            ps.append(points[i])
        else:
            ts.append(None)

    ts2 = []
    for i in range(len(points)):
        if points[i]:
            x, y, z = points[i]
            if u != 0:
                t = (x - x0) / u
            elif v != 0:
                t = (y - y0) / v
            else:
                t = (z - z0) / w
            # print(t)
            # print(points[i])
            # print(min([vertices[j] for j in edges[i][-1]], key=lambda x: x[0])[0])
            # print(max([vertices[j] for j in edges[i][-1]], key=lambda x: x[0])[0])
            # print(min([vertices[j] for j in edges[i][-1]], key=lambda x: x[1])[1])
            # print(max([vertices[j] for j in edges[i][-1]], key=lambda x: x[1])[1])
            # print(min([vertices[j] for j in edges[i][-1]], key=lambda x: x[2])[2])
            # print(max([vertices[j] for j in edges[i][-1]], key=lambda x: x[2])[2])
            if min([vertices[j] for j in edges[i][-1]], key=lambda x: x[0])[0] <= x <= \
                    max([vertices[j] for j in edges[i][-1]], key=lambda x: x[0])[0] and \
                    min([vertices[j] for j in edges[i][-1]], key=lambda x: x[1])[1] <= y <= \
                    max([vertices[j] for j in edges[i][-1]], key=lambda x: x[1])[1] and \
                    min([vertices[j] for j in edges[i][-1]], key=lambda x: x[2])[2] <= z <= \
                    max([vertices[j] for j in edges[i][-1]], key=lambda x: x[2])[2]:
                # print(edges[i], 'sadsda')
                # print(edges[i])
                ts2.append(t)
    # print(ts2)
    ts2 = list(set(ts2))
    # print(ts2)

    min_t, max_t = min(ts2), max(ts2)
    mid_t = (min_t + max_t) / 2
    # print(min_t, mid_t, max_t)

    # min_t, max_t = min(ts2), max(ts2)
    # mid_t = (min_t + max_t) / 2

    tans = []
    # print(len(points), len(edges))
    for edge, point, proj, t in zip(edges, points, projections, ts):
        a, b, c, d = edge[:4]
        edge_points = [vertices[i] for i in edge[4]]
        # print(point)
        if point:
            p1 = (x0, y0, z0)
            v1 = (u, v, w)
            
            # TODO: Пофиксить плохое вычисление краёв цииндра в шаре

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
                        break

            # print(round(r / tan(asin(u * a + v * b + w * c)), 5))
            # if not need:
            # print("ne kurva")
            # print()
            # print(need)
            # print(round(u * a + v * b + w * c, 5))
            # print(round(tan(asin(u * a + v * b + w * c)), 5))
            # print(round(r / tan(asin(u * a + v * b + w * c)), 5))
            # print(t)
            # print(t - abs(round(r / tan(asin(u * a + v * b + w * c)), 5)))
            res = r / tan(asin(u * a + v * b + w * c))
            ins = False
            if res > 0:
                ins = True
            # print(res)
            if t < 0 and res > 0 or t > 0 and res < 0:
                # print("!!!!!")
                res = -res
            # print(res)
            # print(t - res)
            # print(need)
            # print(t - round(r / tan(asin(u * a + v * b + w * c)), 5))
            if need:
                # print(t - round(r / tan(asin(u * a + v * b + w * c)), 5))
                # print(round(t - res, 5))
                tans.append((round(t - res, 5), ins))
            # print(degrees(asin(u * a + v * b + w * c)))
            # print()
        else:
            # print(edge)
            if r > abs(x0 * a + y0 * b + z0 * c + d):
                return "0"

    # tans = list(filter(lambda x: x[0] <= max_t if x[1] else x[0] >= min_t, tans))
    # print(tans)
    # print(list(map(lambda x: min_t <= x[0] <= max_t and x[1], tans)))
    # print(list(map(lambda x: min_t <= x[0] <= max_t and not x[1], tans)))
    # print(len(list(filter(lambda x: x[1], tans))) > 0)
    a = any(list(map(lambda x: min_t <= x[0] <= max_t and x[1], tans)))
    b = any(list(map(lambda x: min_t <= x[0] <= max_t and not x[1], tans)))
    c = len(list(filter(lambda x: x[1], tans))) > 0
    d = len(list(filter(lambda x: not x[1], tans))) > 0
    # print(a, b, c, d, a >= c, b >= d)
    if len(tans) != 0 and not (a >= c and b >= d):
        return "0"
    mx_tn, mn_tn = round(max_t, 5), round(min_t, 5)
    # print(mx_tn, mn_tn)
    # print(tans)
    for tn, is_inside in tans:
        if is_inside and tn < mx_tn:
            mx_tn = tn
        elif not is_inside and tn > mn_tn:
            mn_tn = tn
    # print(mx_tn, mn_tn, 'adasda')
    # min_p, max_p = min(ps), max(ps)
    # print(min_p, max_p)
    # print(ts2)
    # print(len(tans), *[tn for tn in tans])

    # print(tans)
    # print(mn_tn, mx_tn)
    # print(min_t, mid_t, max_t)
    # print()
    # print(len(tans), *[tn for tn in tans])
    # print()
    # print(mn_tn)
    # print(mx_tn)
    # print(123)
    # 1 -0.15892  1.89097
    # 1 -0.15892  1.89097

    # print((maxs) / u, (maxs) / v, (maxs) / w)
    # print((mins) / u, (mins) / v, (mins) / w)

    # t = min_t
    # xp, yp, zp = x0 + u * t, y0 + v * t, z0 + w * t
    # print(xp, yp, zp)
    #
    # t = mid_t
    # xp, yp, zp = x0 + u * t, y0 + v * t, z0 + w * t
    # print(xp, yp, zp)
    #
    # t = max_t
    # xp, yp, zp = x0 + u * t, y0 + v * t, z0 + w * t
    # print(xp, yp, zp)
    # print()
    # print("Finish")
    # print(tans)
    # print()
    # print(mn_tn, mx_tn)

    if mn_tn == mx_tn or mn_tn > max_t or mx_tn < min_t:
        return "0"
    a = [mn_tn, mx_tn]
    return f"1 {min(a)} {max(a)}"


with open("input5.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(input_file))