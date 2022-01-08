"""from time import time
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

    ct = -10000
    t1 = x0 + u * ct + y0 + v * ct + z0 + w * ct

    ct = 10000
    t2 = x0 + u * ct + y0 + v * ct + z0 + w * ct
    ch = t1 <= t2

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

    if ch:
        min_t, max_t = min(ts2), max(ts2)
    else:
        min_t, max_t = max(ts2), min(ts2)
    mid_t = (min_t + max_t) / 2
    # print(min_t, mid_t, max_t, "\n")

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

            # TODO: Пофиксить плохое вычисление краёв цилиндра в шаре

            need = False
            p2 = edge_points[-1]
            v2 = make_ed(subtr(edge_points[-1], edge_points[0]))
            norm = make_ed(vec_multiplication(v1, v2))
            if abs(plosk_by_point_and_norm(p1, norm, p2)) < r:
                need = True

            if not need:
                for i in range(len(edge_points) - 1):
                    p2 = edge_points[i]
                    v2 = make_ed(subtr(edge_points[i], edge_points[i + 1]))
                    norm = make_ed(vec_multiplication(v1, v2))
                    if abs(plosk_by_point_and_norm(p1, norm, p2)) < r:
                        # print(abs(plosk_by_point_and_norm(p1, norm, p2)))
                        # print(123)
                        # print(edge_points[i], edge_points[i + 1])
                        need = True
                        break
            # if need:
                # print(edge)
                # print(p1)
                # print(v1)
                # print(edge_points)
                # return ""

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
            # print(t)
            # print(res)
            # print(mid_t >= t >= max_t)
            # print(t > 0 and res > 0, t < 0 and res < 0, min_t <= t <= mid_t)
            if ch:
                if (res > 0 and min_t <= t <= mid_t) or (res < 0 and mid_t <= t <= max_t):
                    # print("!!!!!")
                    res = -res
            else:
                if (res > 0 and max_t <= t <= mid_t) or (res < 0 and mid_t <= t <= min_t):
                    # print("!!!!!")
                    res = -res
            # print(res)
            # print()
            # print(t - res)
            # print(need)
            # print(t - round(r / tan(asin(u * a + v * b + w * c)), 5))
            if need:
                # print(t - round(r / tan(asin(u * a + v * b + w * c)), 5))
                # print(round(t - res, 5))
                tans.append((t - res, ins))
            # print(degrees(asin(u * a + v * b + w * c)))
            # print()
        else:
            # print(edge)
            if r > abs(x0 * a + y0 * b + z0 * c + d):
                # print(123)
                return "0"

    # tans = list(filter(lambda x: x[0] <= max_t if x[1] else x[0] >= min_t, tans))
    # print(tans)
    # print(list(map(lambda x: min_t <= x[0] <= max_t and x[1], tans)))
    # print(list(map(lambda x: min_t <= x[0] <= max_t and not x[1], tans)))
    # print(len(list(filter(lambda x: x[1], tans))) > 0)
    # print(min_t, max_t)
    # if ch:
    #     a = any(list(map(lambda x: min_t <= x[0] <= max_t and x[1], tans)))
    #     b = any(list(map(lambda x: min_t <= x[0] <= max_t and not x[1], tans)))
    #     # print(1)
    # else:
    #     a = any(list(map(lambda x: min_t >= x[0] >= max_t and x[1], tans)))
    #     b = any(list(map(lambda x: min_t >= x[0] >= max_t and not x[1], tans)))
    # c = len(list(filter(lambda x: x[1], tans))) > 0
    # d = len(list(filter(lambda x: not x[1], tans))) > 0
    # print(a, b, c, d, a >= c, b >= d)
    # print(tans)
    # if len(tans) != 0 and not (a >= c and b >= d):
    #     return "0"

    # print(tans)
    if ch:
        f1, f2 = False, False
        mx_tn, mn_tn = max_t, min_t
        for tn, is_inside in tans:
            if is_inside and tn < mx_tn:
                f1 = True
                mx_tn = tn
            elif not is_inside and tn > mn_tn:
                f2 = True
                mn_tn = tn
        f3 = f1 and f2
    else:
        mn_tn, mx_tn = max_t, min_t
        f1, f2 = False, False
        # print(mx_tn, mn_tn)
        for tn, is_inside in tans:
            if is_inside and tn < mx_tn:
                f1 = True
                mx_tn = tn
            elif not is_inside and tn > mn_tn:
                f2 = True
                mn_tn = tn
        f3 = f1 and f2
    # print(mx_tn, mn_tn, 'adasda')
    # min_p, max_p = min(ps), max(ps)
    # print(min_p, max_p)
    # print(ts2)
    # print(len(tans), *[tn for tn in tans])

    # xp, yp, zp = x0 + u * t, y0 + v * t, z0 + w * t

    # print(*[[x0 + u * tn[0], y0 + v * tn[0], z0 + w * tn[0]] for tn in tans], sep="\n")
    print(*edges, sep="\n")
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

    # if not ch:
    #     mn_tn, mx_tn = mx_tn, mn_tn

    if not ch:
        min_t, max_t = max_t, min_t

    # print(tans)
    # print(ch)
    # print(mn_tn, mx_tn)
    # print(min_t, max_t)

    # print(mn_tn, mx_tn, mn_tn > max_t, mx_tn < min_t)
    if (mn_tn == mx_tn or mn_tn > max_t or mx_tn < min_t) and r != 0:
        return "0"
    a = [mn_tn, mx_tn]
    # print(r)
    # print(abs(min(a)-max(a)))
    # 1 -0.15892  1.89097
    return f"1 {round(min(a), 5)} {round(max(a), 5)}"


with open("inputs/input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(input_file))"""
import random
import time


a = {2: {12: [82, 87], 76: [10, 15]}, 5: {59: [4, 16], 95: [6, 12]}, 48: {10: [1, 89], 90: [10, 20]}}
b = {2: [12, 76], 5: []}
c = [2, 5]

a2 = [[[0.6259509079872594]], [[0.6506000486323554]], [[-0.8687854511821216]], [[0.5345224838248488], [0.5345224838248488]], [[0.8248628195623472]], [[0.747051912764076]], [[-0.7199308899516877]], [[-0.5492104702344917]], [[0.3505902242092289]]]
b2 = [[0.16917592107763765], [-0.5530100413375021], [0.44291023001441493], [-0.8017837257372732, -0.8017837257372731], [0.4124314097811736], [0.4909198283878214], [-0.3039708202018237], [0.4429116695439449], [-0.2726812854960669]]
c2 = [-0.7612916448493695, -0.5204800389058843, -0.22145511500720746, 0.2672612419124244, 0.38665444666985027, 0.4482311476584456, 0.623940104624796, 0.7086586712703119, 0.8959527952013627]
a_x_min, a_x_max, a_y_min, a_y_max, a_z_min, a_z_max = 3, 50, 1, 48, 2, 95


def bin_search_from_to(min_n, max_n, arr, from_id, to_id):
    min_i, max_i = from_id, to_id
    b_b, t_b = 0, 0
    # print(arr)
    while True:
        mid_i = (min_i + max_i) // 2
        # print(min_i, mid_i, max_i)
        # input()
        if arr[mid_i] < min_n:
            min_i = mid_i
            # print(1)
        else:  # arr[mid_i] > min_n:
            if max_i == mid_i:
                # print(1)
                b_b = min_i
                break
            max_i = mid_i
        if max_i - min_i == 1:
            # print(2, arr[min_i], min_n)
            if arr[min_i] >= min_n:
                b_b = min_i
            else:
                b_b = max_i
            break
    min_i, max_i = from_id, to_id

    while True:
        mid_i = (min_i + max_i) // 2
        # print(min_i, mid_i, max_i)
        # input()
        if arr[mid_i] > max_n:
            max_i = mid_i
            # print("gay")
            # print(1)
        else:  # arr[mid_i] > min_n:
            # print("gay again")
            if min_i == mid_i:
                # print(1)
                t_b = max_i
                break
            min_i = mid_i
        if max_i - min_i == 1:
            # print(2, "!!!!!!!!!!!!!!!!!!!!!1")
            # print(max_i, arr)
            if arr[max_i - 1] <= max_n:
                t_b = max_i
            else:
                t_b = min_i
            break

    # print(b_b, t_b)
    return b_b, t_b


def search_in_z(ind1, ind2, a_z_min, a_z_max):
    # print(a2[ind1][ind2])
    z_min, z_max = bin_search_from_to(a_z_min, a_z_max, a2[ind1][ind2], 0, len(a2[ind1][ind2]))
    # print(z_max - z_min + 1)
    return z_max - z_min + 1


def search_in_y(ind, a_y_min, a_y_max, a_z_min, a_z_max):
    res = 0
    y_min, y_max = bin_search_from_to(a_y_min, a_y_max, b2[ind], 0, len(b2[ind]))
    # print(y_min, y_max, "!!!")
    for i in range(y_min, y_max):
        # print(i, "Y")
        res += search_in_z(ind, i, a_z_min, a_z_max)
    return res


def search_in_x(a_x_min, a_x_max, a_y_min, a_y_max, a_z_min, a_z_max):
    res = 0
    x_min, x_max = bin_search_from_to(a_x_min, a_x_max, c2, 0, len(c2))
    for i in range(x_min, x_max):
        res += search_in_y(i, a_y_min, a_y_max, a_z_min, a_z_max)
    return res


for i in range(min(len(min_angs), len(max_angs))):
    print(search_in_x(min_angs[i][0], max_angs[i][0], min_angs[i][1], max_angs[i][1], min_angs[i][2], max_angs[i][2]))
# a_x_min, a_x_max, a_y_min, a_y_max, a_z_min, a_z_max = 3, 50, 1, 48, 2, 95
# print(search_in_x(a_x_min, a_x_max, a_y_min, a_y_max, a_z_min, a_z_max))


# arr = [random.choice(range(1, 10)) for i in range(1, 10001)]
# t = time.time()
# print(arr[arr.index(42051)])
# print(time.time() - t)
#
# print(arr[9999])
# arr.sort()
# print(arr)
# print(arr)
# t = time.time()
# res = bin_search_from_to(0.2, 24.7, arr, 0, len(arr))
# print(res)
# print(arr[res[0]], arr[res[1]])
# print(time.time() - t)