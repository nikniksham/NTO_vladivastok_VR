with open('input7.obj') as r:
    vertexes = []
    edges = []
    from_zero = True
    for line in r.readlines():
        if line.startswith('v '):
            vertexes.append(tuple(map(float, line[2:].split())))
        if line.startswith('f '):
            edges.append(tuple(map(lambda x: int(x.split('/')[0]) - (1 if from_zero else 0), line[2:].split())))
    print(len(vertexes))
    for vertex in vertexes:
        print(*vertex)
    print()
    print(len(edges))
    for edge in edges:
        print(len(edge), *edge)
