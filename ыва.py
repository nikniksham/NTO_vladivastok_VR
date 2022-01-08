from math import pi, sin, cos, radians
# from time import time
# t = time()

vec_abs = lambda vec3: sum(map(lambda x: x**2, vec3))**0.5
vec_invert = lambda a: [-a[0], -a[1], -a[2]]
vec_subtraction = lambda a, b: [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
vec_addition = lambda a, b: [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
vec_multiplication = lambda a, b: [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
vec_multiplication_by_const = lambda a, b: [a[0]*b, a[1]*b, a[2]*b]
vec_ed_angle = lambda a, b: a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
mult_matr3_vec3 = lambda m, v: [m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2], m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2], m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2]]


def make_ed(vec3):
    abs = vec_abs(vec3)
    return [vec3[0]/abs, vec3[1]/abs, vec3[2]/abs]


def logic(data):
    R = data[0][0]
    W = radians(data[0][1])*0.005
    cam_pos = data[1]
    cam_forward = make_ed(data[2])
    cam_top = make_ed(data[3])
    cam_right = vec_multiplication(cam_top, cam_forward)
    to_mountain = vec_invert(cam_pos)
    if (abs(vec_ed_angle(to_mountain, cam_right) / vec_ed_angle(to_mountain, cam_forward)) > 1 and abs(vec_ed_angle(to_mountain, cam_top) / vec_ed_angle(to_mountain, cam_forward)) > 1) or vec_ed_angle(cam_forward, make_ed(to_mountain)) < 0:
        return '-1'
    c = (vec_abs(cam_pos)**2 - R**2)**0.5
    max_visible = 0
    visibles = []
    ang = 0
    vis_t = 0
    t = -0.005
    while abs(ang) < 2*pi:
        t += 0.005
        ang += W
        # print(ang)
        matrix = [
            [cos(ang), -sin(ang), 0],
            [sin(ang), cos(ang), 0],
            [0,  0,  1]
        ]
        visible = 0
        visible_mountain = []
        for i, mountain in enumerate(data[5:]):
            mountain_pos = mult_matr3_vec3(matrix, vec_multiplication_by_const(make_ed(mountain[:3]), R + mountain[3]))
            a = ((R + mountain[3])**2 - R**2)**0.5
            to_mountain = vec_subtraction(mountain_pos, cam_pos)
            if vec_abs(to_mountain) > c + a:
                continue
            if abs(vec_ed_angle(to_mountain, cam_right) / vec_ed_angle(to_mountain, cam_forward)) <= 1 and abs(vec_ed_angle(to_mountain, cam_top) / vec_ed_angle(to_mountain, cam_forward)) <= 1 and vec_ed_angle(cam_forward, make_ed(to_mountain)) > 0:
                visible += 1
                visible_mountain.append(i+1)
        if visible > max_visible:
            visibles = visible_mountain
            max_visible = visible
            vis_t = t
        if visible == len(data[5:]):
            return str(vis_t) + '\n' + str(max_visible) + '\n' + '\n'.join(map(str, visibles))
    if max_visible == 0:
        return '-1'
    return str(vis_t) + '\n' + str(max_visible) + '\n' + '\n'.join(map(str, visibles))


with open('input.txt') as r:
    lines = list(map(lambda l: list(map(float, l.split())), r.readlines()))

res = logic(lines)

with open('output.txt', 'w') as w:
    w.write(res)
# print(time() - t)