from Solution_first_problem import calculate

tests = [
    ['tests/test_1.txt', '1 -0.15892 1.89097'],
    ['tests/test_2.txt', '1 0.54819 1.18386'],
    ['tests/test_3.txt', '1 -0.15892 1.89097'],
    ['tests/test_4.txt', '0'],
    ['tests/test_5.txt', '0'],
    ['tests/test_6.txt', '1 86601.51543 86603.56532'],
    ['tests/test_7.txt', '1 -86603.56532 -86601.51543'],
    ['tests/test_8.txt', '1 -1.0 1.0'],
    ['tests/test_9.txt', '1 -1.0 0.43431'],
    ['tests/test_10.txt', '1 -1.0 -0.41421'],
    ['tests/test_11.txt', '1 -1.0 -0.9799'],
    ['tests/test_12.txt', '0'],
    ['tests/test_13.txt', '0'],
    ['tests/test_14.txt', '1 -0.27344 0.27344'],
    ['tests/test_15.txt', '0'],
    ['tests/test_16.txt', '1 -1.0 1.0'],
    ['tests/test_17.txt', '1 -1.00275 1.00275'],
    ['tests/test_18.txt', '1 -0.61421 0.61421'],
    ['tests/test_19.txt', '0'],
    ['tests/test_20.txt', '1 -0.71716 1.3367'],
    ['tests/test_21.txt', '1 0.41421 1.11486'],
    ['tests/test_22.txt', '1 -1.0 1.39216'],
    ['tests/test_23.txt', '0'],
    ['tests/test_24.txt', '0']
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