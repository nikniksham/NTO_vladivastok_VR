import copy
import time


def recr_calculate(det, mnoj):
    if len(det) == 2:
        return mnoj * (det[0][0] * det[1][1] - det[1][0] * det[0][1])
    res = 0
    for loop in range(len(det[0])):
        new_mnoj = det[0][loop] * (1 if loop % 2 == 0 else -1)
        new_det = copy.deepcopy(det)
        new_det.pop(0)
        for i in range(len(new_det)):
            new_det[i].pop(loop)
        res += recr_calculate(new_det, new_mnoj)
        # print(a, res)
        # res += a
        # print(res)
    return mnoj * res


# t1 = time.time()
# det = [[-4, -2, -7, 8, 4], [2, 7, 4, 9, 8], [2, 0, 6, -3, 17], [6, 4, -10, -4, 2], [5, 11, -7, 0, -9]]
# print(recr_calculate(det, 1))
# print(time.time() - t1)
n = int(input())
det = []
for i in range(n):
    # det.append(list(map(int, input().split())))  # 2
    nr = []  # 1
    for j in range(n):
        nr.append(int(input()))
    det.append(nr)
# print(det)
print(recr_calculate(det, 1))