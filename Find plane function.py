def subtr(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]


def scalar(ver1, ver2):
    return ver1[0] * ver2[0] + ver1[1] * ver2[1] + ver1[2] * ver2[2]


p0 = (-1, -1, -1)
p1, p2 = subtr([-1, -1, 1], p0), subtr([-1, 1, 1], p0)
a, b, c = (p1[1] * p2[2] - p1[2] * p2[1]), -(p1[0] * p2[2] - p1[2] * p2[0]), (p1[0] * p2[1] - p1[1] * p2[0])
d = -p0[0] * a - p0[1] * b - p0[2] * c
print([a, b, c, d])

# u, v, w = [2, -3, 1]
# ds = [1, 3, 2]
# m0 = [-u, -v, -w]
# # vec = [d, d, d]
# points = []
# edges = [[0, 2, -1, -11]]
# for edge in edges:
#     vec_pl = [edge[1], edge[2], edge[3]]
#     scl = scalar(ds, vec_pl)
#     if scl != 0:
#         # xp, yp, zp = d + m0[0], d + m0[1], d + m0[2]
#         t = edge[0] * ds[0] + edge[1] * ds[1] + edge[2] * ds[2]
#         oth = edge[0] * m0[0] + edge[1] * m0[1] + edge[2] * m0[2] + edge[3]
#         print(t, oth)
#         t = -oth / t
#         print(t)
#         xp, yp, zp = t * ds[0] + m0[0], t* ds[1] + m0[1], t* ds[2] + m0[2]
#         print(xp, yp, zp)