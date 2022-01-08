def clamp_ang(ang):
    if 1.0 >= ang >= -1.0:
        # print('aaa')
        return ang
    elif ang > 1.0:
        return -2.0 + ang
    else:
        return -2.0 - ang

print(clamp_ang())