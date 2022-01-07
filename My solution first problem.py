class Vec:
    def __init__(self, coord):
        self.x, self.y, self.z = coord

    def to_single(self):
        self_len = self.get_len()
        return Vec([self.x / self_len, self.y / self_len, self.z / self_len])

    def get_single_angle(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def get_len(self):
        return sum(map(lambda x: x**2, [self.x, self.y, self.z]))**0.5

    def __mul__(self, other):
        if type(other) is Vec:
            return Vec([self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x])
        else:
            return Vec([self.x * other, self.y * other, self.z * other])

    def __sub__(self, other):
        return Vec([self.x - other.x, self.y - other.y, self.z - other.z])

    def __add__(self, other):
        return Vec([self.x + other.x, self.y + other.y, self.z + other.z])

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.z}]"


def multiply_matrix(matrix):
    return matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1]*matrix[1][2]*matrix[2][0] + \
           matrix[0][2]*matrix[1][0]*matrix[2][1] - matrix[0][2]*matrix[1][1]*matrix[2][0] - \
           matrix[0][1]*matrix[1][0]*matrix[2][2] - matrix[0][0]*matrix[1][2]*matrix[2][1]


def calculate(input_file):
    R = input_file[0][0]
    cam_coord = Vec(input_file[1])
    vec_forward = Vec(input_file[2]).to_single()
    vec_top = Vec(input_file[3]).to_single()
    vec_right = vec_top * vec_forward
    break_point = (cam_coord.get_len()**2 - R**2)**0.5
    result = []
    for number, mountain in enumerate(input_file[5:], start=1):
        mountain_coord = Vec(mountain[:3]).to_single() * (R + mountain[3])
        mountain_break_point = ((R + mountain[3])**2 - R**2)**0.5
        vec_to_mountain = mountain_coord - cam_coord
        if vec_to_mountain.get_len() <= break_point + mountain_break_point:
            p1 = mountain_coord
            p2 = p1 + vec_top
            p3 = p1 + vec_right
            matrix = [
                [cam_coord.x - p1.x, cam_coord.y - p1.y, cam_coord.z - p1.z],
                [p2.x - p1.x, p2.y - p1.y, p2.z - p1.z],
                [p3.x - p1.x, p3.y - p1.y, p3.z - p1.z]
            ]
            dist = multiply_matrix(matrix)
            project_point = Vec([input_file[1][0] + vec_forward.x * dist, input_file[1][1] + vec_forward.y * dist, input_file[1][2] + vec_forward.z * dist])
            vec_to_mount = mountain_coord - project_point
            to_mount_abs = vec_to_mount.get_len()
            if vec_to_mount.get_single_angle(vec_top) == 0 or vec_to_mount.get_single_angle(vec_right) == 0:
                if to_mount_abs <= dist:
                    result.append(number)
            else:
                cos_a = 1/(1+(vec_to_mount.get_single_angle(vec_right)/vec_to_mount.get_single_angle(vec_top))**2)**0.5
                sin_a = (1 - cos_a**2)**0.5
                if abs(to_mount_abs * cos_a) <= dist and abs(to_mount_abs * sin_a) <= dist:
                    result.append(number)
    return "\n".join(map(str, [len(result)]+result))


with open("inputs/input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        output_file.write(calculate(list(map(lambda l: list(map(float, l.split())), input_file.readlines()))))
