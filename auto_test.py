from Solution_first_problem import calculate

tests = [
    ['input.txt', '1 -0.15892 1.89097'],
]

is_only_wrong = False

for i, test in enumerate(tests):
    file, result = test
    with open(file, 'r') as f:
        res = calculate(f)
    if res == result and not is_only_wrong:
        print(f'test №{i+1} OK')
    if res != result:
        print(f'\ntest №{i+1} WA\nAnswer: {res}\nTrue:   {result}\n')