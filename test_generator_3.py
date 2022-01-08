from random import randrange

planets = 10**5
oculus = 10**4

with open('input.txt', 'w') as w:
    w.write(f'{planets}\n')
    for i in range(planets):
        w.write(f'{randrange(-(10**6), 10**6)} {randrange(-(10**6), 10**6)} {randrange(-(10**6), 10**6)}\n')
    w.write('\n')
    w.write(f'{oculus}\n')
    for i in range(oculus):
        w.write(f'{randrange(-(10**6), 10**6)} {randrange(-(10**6), 10**6)} {randrange(-(10**6), 10**6)} {randrange(10**6)}\n')