def get_len(x, y, z):
    return (x*x + y*y + z*z)**0.5


def calculate(input_file):
    points = []
    for i in range(int(input_file.readline())):
        points.append(tuple(map(int, input_file.readline().split())))
    input_file.readline()
    a = int(input_file.readline())
    result = [""]*a
    for _ in range(a):
        count = 0
        u, v, w, r = map(int, input_file.readline().split())
        oc_l = (u*u + v*v + w*w)**0.5
        first_cos = oc_l / (oc_l*oc_l + r*r)**0.5
        u = u/oc_l
        v = v/oc_l
        w = w/oc_l
        for x, y, z in points:
            self_len = get_len(x, y, z)
            if self_len == 0:
                count += 1
                continue
            # ed_vec_p = (point[0] / self_len, point[1] / self_len, point[2] / self_len)
            if (x*u+ y*v + z*w)/self_len >= first_cos:
                count += 1
        result[_] = str(count)
    return '\n'.join(result)


with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(input_file))