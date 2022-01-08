from time import time
t_st = time()
a = []
b = []
c = []


def bin_search_from_to(min_n, max_n, arr, from_id, to_id):
    min_i, max_i = from_id, to_id
    b_b, t_b = 0, 0
    # print(arr)
    while True:
        mid_i = (min_i + max_i) // 2
        if arr[mid_i] < min_n:
            min_i = mid_i
            # print(1)
        else:  # arr[mid_i] > min_n:
            if max_i == mid_i:
                # print(1)
                b_b = min_i
                break
            max_i = mid_i
        if max_i - min_i < 2:
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
        if max_i - min_i < 2:
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
    z_min, z_max = bin_search_from_to(a_z_min, a_z_max, a[ind1][ind2], 0, len(a[ind1][ind2]))
    return z_max - z_min + 1


def search_in_y(ind, a_y_min, a_y_max, a_z_min, a_z_max):
    res = 0
    y_min, y_max = bin_search_from_to(a_y_min, a_y_max, b[ind], 0, len(b[ind]))
    # print(y_min, y_max, "!!!")
    for i in range(y_min, y_max):
        # print(i, "Y")
        res += search_in_z(ind, i, a_z_min, a_z_max)
    return res


def search_in_x(a_x_min, a_x_max, a_y_min, a_y_max, a_z_min, a_z_max):
    res = 0
    x_min, x_max = bin_search_from_to(a_x_min, a_x_max, c, 0, len(c))
    # print(x_min, x_max)
    for i in range(x_min, x_max):
        res += search_in_y(i, a_y_min, a_y_max, a_z_min, a_z_max)
    return res


def to_single(arr, arr_len):
    return [arr[0] / arr_len, arr[1] / arr_len, arr[2] / arr_len]


def get_single_angle(arr1, arr2):
    return arr1[0] * arr2[0] + arr1[1] * arr2[1] + arr1[2] * arr2[2]


def clamp_ang(ang):
    if 1.0 >= ang >= -1.0:
        return ang
    elif ang > 1.0:
        return -2.0 + ang
    else:
        return -2.0 - ang


def calculate(input_file):
    result = []
    points = []
    for i in range(1, int(input_file[0][0]) + 1):
        poi = input_file[i]
        # x = to_single(a, get_len(a))
        # print(int(x[0]*10**5+10**6)*10**12+int(x[0]*10**5+10**6)*10**6+int(x[0]*10**5+10**6), x, sep='\n')
        points.append(to_single(poi, (poi[0]*poi[0] + poi[1]*poi[1] + poi[2]*poi[2])**0.5))
    points.sort(key=lambda x: x[0])
    last_x, last_y = -1, -1
    # print(*points, sep='\n')
    for x, y, z in points:
        if x != last_x:
            # print(x, y, z)
            c.append(x)
            b.append([y])
            a.append([[z]])
        else:
            if y != last_y:
                b[-1].append(y)
                a[-1].append([z])
            else:
                a[-1][-1].append(z)
        last_x, last_y = x, y
    for spis in b:
        spis.sort()
    for spis in a:
        for pod_spis in spis:
            pod_spis.sort()
    print(a)
    print(b)
    print(c)
    for u, v, w, r in input_file[len(points)+3:]:
        ocular_coord = (u, v, w)
        oc_l = (ocular_coord[0]*ocular_coord[0] + ocular_coord[1]*ocular_coord[1] + ocular_coord[2]*ocular_coord[2])**0.5
        hyp = (oc_l*oc_l + r*r)**0.5
        first_cos = oc_l / hyp
        ed_vec_oc = to_single(ocular_coord, oc_l)
        min_ang = tuple(map(lambda x: clamp_ang(x - first_cos), ed_vec_oc))
        max_ang = tuple(map(lambda x: clamp_ang(x + first_cos), ed_vec_oc))
        print(min_ang)
        print(max_ang)
        print(search_in_x(min_ang[0], max_ang[0], min_ang[1], max_ang[1], min_ang[2], max_ang[2]))
        # print('min_ang', *map(lambda x: clamp_ang(x + first_cos), ed_vec_oc))
        # print('max_ang', *map(lambda x: clamp_ang(x - first_cos), ed_vec_oc))

        # for i in range(20):
        #     pass

        # for point in points:
        #     self_len = get_len(point)
        #     if self_len == 0:
        #         count += 1
        #         continue
        #     ed_vec_p = to_single(point, self_len)
        #     sc_m = get_single_angle(ed_vec_p, ed_vec_oc)
        #     if sc_m >= first_cos:
        #         count += 1
        # result.append(str(count))

    return "\n".join(result)


with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(list(map(lambda l: list(map(float, l.split())), input_file.readlines()))))

print(time() - t_st)
"""
90 90 90
89 80 70
88 70 50
87 60 30
77 40 10


a = [[[82, 87], [10, 15]], [[4, 16], [6, 12]], [[1, 89], [10, 20]]]
b = [[12, 16], [59, 95], [10, 90]]
c = [2, 5, 48]
# [63.71019, 123.31286, 123.31286, 63.71019]
"""














