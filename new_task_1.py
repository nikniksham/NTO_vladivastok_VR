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


class Direct:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vec = Vec((start[0] - end[0], start[1] - end[1], start[2] - end[2]))

    def __repr__(self):
        return f"Start in {self.start}, end in {self.end}"


def calculate(input_file):
    vertexes = []
    for i in range(int(input_file[0][0])):
        vertexes.append(input_file[i + 1])
    ribs = []
    edges = []
    for j in range(int(input_file[len(vertexes) + 1][0])):
        arr = list(map(int, input_file[len(vertexes) + 2 + j][1:]))
        edges.append(arr)
        for ind in range(len(arr) - 1):
            ribs.append(Direct(vertexes[arr[ind]], vertexes[arr[ind + 1]]))
        ribs.append(Direct(vertexes[arr[-1]], vertexes[arr[0]]))
    print(edges, sep="\n")
    print()
    print(*ribs, sep="\n")
    return ""


with open("inputs/input2.txt", "r") as input_file:
    with open("output2.txt", "w") as output_file:
        output_file.write(calculate(list(filter(lambda x: x != [], map(lambda l: list(map(float, l.split())), input_file.readlines())))))
