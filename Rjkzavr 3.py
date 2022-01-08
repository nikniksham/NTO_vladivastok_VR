from time import time
from math import degrees, acos


def to_single(arr, arr_len):
    return [round(arr[0] / arr_len, 5), round(arr[1] / arr_len, 5), round(arr[2] / arr_len, 5)]


def get_single_angle(arr1, arr2):
    return arr1[0] * arr2[0] + arr1[1] * arr2[1] + arr1[2] * arr2[2]


def get_len(arr):
    return sum(map(lambda x: x**2, arr))**0.5


def calculate(input_file):
    result = []
    points = []
    for i in range(1, int(input_file[0][0]) + 1):
        a = input_file[i]
        # x = to_single(a, get_len(a))
        # print(int(x[0]*10**5+10**6)*10**12+int(x[0]*10**5+10**6)*10**6+int(x[0]*10**5+10**6), x, sep='\n')
        points.append(to_single(a, get_len(a)))
    print()
    t_st = time()
    points.sort(key=lambda x: x[0])
    print(time() - t_st)
    for u, v, w, r in input_file[len(points)+3:]:
        count = 0
        ocular_coord = (u, v, w)
        oc_l = get_len(ocular_coord)
        hyp = (oc_l**2 + r**2)**0.5
        first_cos = oc_l / hyp
        ed_vec_oc = to_single(ocular_coord, oc_l)
        print('min_ang', *map(lambda x: degrees(acos(x) + acos(first_cos)) , ed_vec_oc))
        print('max_ang', *map(lambda x: degrees(acos(x) - acos(first_cos)) , ed_vec_oc))
        for point in points:
            self_len = get_len(point)
            if self_len == 0:
                count += 1
                continue
            ed_vec_p = to_single(point, self_len)
            sc_m = get_single_angle(ed_vec_p, ed_vec_oc)
            if sc_m >= first_cos:
                count += 1
        result.append(str(count))

    return "\n".join(result)


with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(list(map(lambda l: list(map(float, l.split())), input_file.readlines()))))

"""
90 90 90
89 80 70
88 70 50
87 60 30
77 40 10
"""