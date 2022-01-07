from math import tan, asin, sin, acos
from time import time
st = time()

vec_subtraction = lambda a, b: [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
vec_addition = lambda a, b: [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
vec_multiplication_by_const = lambda a, b: [a[0]*b, a[1]*b, a[2]*b]
scalar = lambda a, b: a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
mult_matr3_vec3 = lambda m, v: [m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2], m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2], m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2]]
vec_abs = lambda vec3: sum(map(lambda x: x**2, vec3))**0.5
vec_multiplication = lambda a, b: [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
plosk_by_point_and_norm = lambda m, n, p: n[0]*(p[0] - m[0]) + n[1]*(p[1] - m[1]) + n[2]*(p[2] - m[2])
dist_point_plane = lambda po, pl: po[0]*pl[0] + po[1]*pl[1] + po[2]*pl[2] + pl[3]
get_d = lambda p1, p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5
check_in_figure = lambda point, edges: all([dist_point_plane(point, edge) <= 0 for edge in edges])
center_figure = lambda vertexes: (round(sum([x for x, y, z in vertexes])/len(vertexes), 3),
                                  round(sum([y for x, y, z in vertexes])/len(vertexes), 3),
                                  round(sum([z for x, y, z in vertexes])/len(vertexes), 3))


def make_ed(ver):
    le = vec_abs(ver)
    if le != 0:
        return ver[0] / le, ver[1] / le, ver[2] / le
    return [0, 0, 0]


def calculate(file):
    # считываем точки
    count_vertices = int(file.readline())
    vertices = []
    for _ in range(count_vertices):
        vertices.append(tuple(map(float, file.readline().split())))

    # ищем цент фигуры
    center = center_figure(vertices)
    # print(' '.join(tuple(map(lambda x: str(round(x, 5)).ljust(7, ' '), center))))

    # хз зачем
    file.readline()

    # считываем грани
    count_edge = int(file.readline())
    edges = []
    for _ in range(count_edge):
        arr = list(map(int, file.readline().split()))[1:]
        p0 = vertices[arr[0]]
        p1 = vertices[arr[1]]
        p2 = (0, 0, 0)
        for ver_id in arr[2:]:
            p2 = vertices[ver_id]
            if round(get_d(p0, p2) + get_d(p1, p2) - get_d(p0, p1), 6) * round(
                    get_d(p0, p2) + get_d(p0, p1) - get_d(p1, p2), 6) * round(
                get_d(p0, p1) + get_d(p1, p2) - get_d(p0, p2), 6) != 0:
                break
        # print(p0, p1, p2,)
        # составляем уравнение плоскости для каждой грани
        p1 = vec_subtraction(p0, p1)
        p2 = vec_subtraction(p0, p2)
        a, b, c = (p1[1] * p2[2] - p1[2] * p2[1]), -(p1[0] * p2[2] - p1[2] * p2[0]), (p1[0] * p2[1] - p1[1] * p2[0])
        a, b, c = make_ed((a, b, c))
        d = -p0[0] * a - p0[1] * b - p0[2] * c
        # print(center)
        # print(dist_point_plane(center, (a, b, c, d)))
        if int(dist_point_plane(center, (a, b, c, d))) > 0:
            a, b, c, d = -a, -b, -c, -d
        # print(a, b, c)
        edges.append([a, b, c, d, arr])

    # хз зачем
    file.readline()

    # считываем данные цилиндра
    cylinder_point = tuple(map(float, file.readline().split()))
    cylinder_vec = make_ed(tuple(map(float, file.readline().split())))
    cylinder_radius = float(file.readline())
    # d = vec_abs((u, v, w))
    # cylinder_vec = u/d, v/d, w/d
    # print(' '.join(tuple(map(lambda x: str(round(x, 5)).ljust(7, ' '), cylinder_point))), ' '.join(tuple(map(lambda x: str(round(x, 5)).ljust(7, ' '), cylinder_vec))), str(round(cylinder_radius, 5)).ljust(7, ' '), sep='\n')

    # тест функции точка в фигуре
    # в кубе: top, back, left, up, right, down
    # print("Тест точки в фигуре")
    # print('left', 'right', 'back', 'up  ', 'top ', 'down', sep='\t')
    # print(center)
    # print(check_in_figure(center, edges), sep='\t')
    # for x in range(-1, 2):
    #     for y in range(-1, 2):
    #         for z in range(-1, 2):
    #             print(check_in_figure((x, y, z), edges), sep='\t')
    # print(check_in_figure((-1, -1, -1.1), edges), sep='\t')
    # print(check_in_figure((1, 1, 1), edges), sep='\t')

    # находим и проверяем все точки пересечения с плоскостями цилиндра
    inside, outside = 0, 0
    result = []
    for edge in edges:
        ang = scalar(edge[:4], cylinder_vec)
        if ang == 0 and cylinder_radius > abs(plosk_by_point_and_norm(vertices[edge[4][0]], edge[:4], cylinder_point)):
            # if cylinder_radius > plosk_by_point_and_norm(vertices[edge[4][0]], edge[:4], cylinder_point):
            # print(vertices[edge[4][0]], edge[:4], cylinder_point)
            # input()
            # print(edge, plosk_by_point_and_norm(vertices[edge[4][0]], edge[:4], cylinder_point))
            # print(abs(plosk_by_point_and_norm(vertices[edge[4][0]], edge[:4], cylinder_point)))
            # print("Не влазим!")
            return "0"
        elif ang != 0:
            t = edge[0] * cylinder_vec[0] + edge[1] * cylinder_vec[1] + edge[2] * cylinder_vec[2]
            oth = edge[0] * cylinder_point[0] + edge[1] * cylinder_point[1] + edge[2] * cylinder_point[2] + edge[3]
            # print(edge)
            # print(t, oth, ang)
            t = -oth / t
            # print(t)
            cross_point = t * cylinder_vec[0] + cylinder_point[0], t * cylinder_vec[1] + cylinder_point[1], t * cylinder_vec[2] + cylinder_point[2]
            if abs(ang) != 1:
                # тк не перпендикулярно, можем спроецировать прямую в грань и проверить, что точка лежит в фигуре
                otcl = -edge[0] * cylinder_point[0] + -edge[1] * cylinder_point[1] + -edge[2] * cylinder_point[2] - edge[3]
                point = [edge[0] * otcl + cylinder_point[0], edge[1] * otcl + cylinder_point[1], edge[2] * otcl + cylinder_point[2]]
                direction = make_ed(vec_subtraction(point, cross_point))
                if plosk_by_point_and_norm(cylinder_point, cylinder_vec, cross_point) < 0:
                    ang = -ang
                check_point = vec_addition(vec_multiplication_by_const(direction, cylinder_radius / ang), cross_point)
                # print("Эта штука не перпендикулярна, надо делать проекцию и проверять, что результат в фигуре (на границе)")
                # print(cross_point, abs(degrees(acos(ang))-90), ang)
                # print(subtr([-a * otcl + x0, -b * otcl + y0, -c * otcl + z0], point), point)
                # вторая точка
                # print(edge[:4], point)
                # print(otcl)
                # print(edge[0] * cross_point[0] + edge[1] * cross_point[1] + edge[2] * cross_point[2] + edge[3])
                # print(edge[0] * point[0] + edge[1] * point[1] + edge[2] * point[2] + edge[3])
                # print(cross_point, point)
                # print(vec_subtraction(point, cross_point))
                # print(cross_point, edge[:3])
                # print(cross_point, '???')
                # print(scalar(cylinder_vec, edge[:3]))
                # print('out' if scalar(cylinder_vec, edge[:3]) > 0 else 'in')
                # print(cylinder_radius / ang, ang)
                # print(direction, ang)
                # print(vec_multiplication_by_const(direction, cylinder_radius / ang))
                # print(edge[:3])
                # print(check_point, plosk_by_point_and_norm(cylinder_point, cylinder_vec, check_point))
                # for edge in edges:
                #     print(edge, check_point)
                #     print(dist_point_plane(check_point, edge))
                # print(plosk_by_point_and_norm(cylinder_point, cylinder_vec, check_point), check_in_figure(check_point, edges))
                if check_in_figure(check_point, edges):
                    # print(check_point)
                    t = round(plosk_by_point_and_norm(cylinder_point, cylinder_vec, check_point), 5)
                    if cylinder_radius / tan(asin(scalar(cylinder_vec, edge[:3]))) > 0:
                        outside = t
                    else:
                        inside = t
            else:
                # print("Эта штука перпендикулярна, надо проверять, что круг влазит в грань")
                good = True
                for index in range(len(edge[4])):
                    # p1 = cross_point
                    # v1 = cylinder_vec
                    # p2 = vertices[edge[4][0]]
                    # v2 = make_ed(vec_subtraction(vertices[edge[4][index]], vertices[edge[4][(index + 1) % len(edge[4])]]))
                    # norm = make_ed(vec_multiplication(v1, v2))
                    # print(vertices[edge[4][index]][1:], vertices[edge[4][(index + 1) % len(edge[4])]][1:])
                    # print(cylinder_point[1:])
                    # print(v1, v2)
                    # print(vertices[edge[4][index]], norm)
                    # print(abs(plosk_by_point_and_norm(cross_point, make_ed(vec_multiplication(cylinder_vec, make_ed(vec_subtraction(vertices[edge[4][index]], vertices[edge[4][(index + 1) % len(edge[4])]])))), vertices[edge[4][index]])))
                    if cylinder_radius > abs(plosk_by_point_and_norm(cross_point, make_ed(vec_multiplication(cylinder_vec, make_ed(vec_subtraction(vertices[edge[4][index]], vertices[edge[4][(index + 1) % len(edge[4])]])))), vertices[edge[4][index]])):
                        good = False
                        break
                    # print()
                if not good:
                    # print("Радиус НЕ влез!")
                    pass
                else:
                    x, y, z = cross_point
                    if cylinder_vec[0] != 0:
                        t = (x - cylinder_point[0]) / cylinder_vec[0]
                        # print(1, t)
                    elif cylinder_vec[1] != 0:
                        t = (y - cylinder_point[1]) / cylinder_vec[1]
                        # print(2, t)
                    else:
                        t = (z - cylinder_point[2]) / cylinder_vec[2]
                    if t not in result:
                        result.append(round(t, 5))

    # проверка, что есть точки и вывод итогового ответа
    if len(result) == 2:
        # print(result)
        return '1 ' + ' '.join(map(str, sorted(result)))
    elif len(result) == 1:
        return '1 ' + ' '.join(map(str, sorted([result[0], (inside if inside else outside)])))
    elif len(result) == 0:
        if inside < outside:
            return f'1 {inside} {outside}'
        else:
            return '0'
    else:
        return '0'


if __name__ == '__main__':
    with open("inputs/input.txt", "r") as input_file:
        with open("output.txt", "w") as output_file:
            output_file.write(calculate(input_file))