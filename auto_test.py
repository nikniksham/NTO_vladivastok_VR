from Solution_first_problem import calculate

tests = [
    ['Tinput1.txt', '1'],
    ['Tinput2.txt', '0'],
    ['Tinput1.txt', '1'],
    ['Tinput1.txt', '1'],
    ['Tinput1.txt', '1'],
    ['Tinput2.txt', '0'],
    ['Tinput1.txt', '1'],
    ['Tinput1.txt', '1'],
    ['Tinput1.txt', '1'],
]


def calculate(t):
    return '1'


is_only_wrong = True

for i, test in enumerate(tests):
    file, result = test
    if calculate(file) == result and not is_only_wrong:
        print(f'test №{i+1} OK')
    elif calculate(file) != result:
        print(f'\ntest №{i+1} WA\nAnswer: {calculate(file)}\nTrue:   {result}\n')