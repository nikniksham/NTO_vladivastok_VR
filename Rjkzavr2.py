vec_abs = lambda vec3: sum(map(lambda x: x**2, vec3))**0.5
vec_subtraction = lambda a, b: [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
vec_addition = lambda a, b: [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
vec_multiplication = lambda a, b: [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
vec_multiplication_by_const = lambda a, b: [a[0]*b, a[1]*b, a[2]*b]
vec_ed_angle = lambda a, b: a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def make_ed(vec3):
    abs = vec_abs(vec3)
    return [vec3[0]/abs, vec3[1]/abs, vec3[2]/abs]


def logic(data):
    R = data[0][0]
    planet_pos = [0, 0, 0]
    cam_pos = data[1]
    cam_forward = make_ed(data[2])
    cam_top = make_ed(data[3])
    cam_right = vec_multiplication(cam_top, cam_forward)
    c = (vec_abs(cam_pos)**2 - R**2)**0.5
    res = []
    for i, mountain in enumerate(data[5:]):
        mountain_pos = vec_multiplication_by_const(make_ed(mountain[:3]), R + mountain[3])
        a = ((R + mountain[3])**2 - R**2)**0.5
        to_mountain = vec_subtraction(mountain_pos, cam_pos)
        if vec_abs(to_mountain) > c + a:
            continue
        if abs(vec_ed_angle(to_mountain, cam_right) / vec_ed_angle(to_mountain, cam_forward)) <= 1 and abs(vec_ed_angle(to_mountain, cam_top) / vec_ed_angle(to_mountain, cam_forward)) <= 1 and vec_ed_angle(cam_forward, make_ed(to_mountain)) > 0:
            res.append(i+1)
    return "\n".join(map(str, [len(res)]+res))


with open('input.txt') as r:
    lines = list(map(lambda l: list(map(float, l.split())), r.readlines()))

res = logic(lines)

with open('output.txt', 'w') as w:
    w.write(res)