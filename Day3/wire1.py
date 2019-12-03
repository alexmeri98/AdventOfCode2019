from collections import defaultdict

with open('input.data','r') as f:
    paths = [line.split(',') for line in f.readlines()]
    
    wires = defaultdict()
    wireId = 1
    for path in paths:
        wires[wireId] = [(0,0)]
        for movement in path:
            direction = movement[0]
            distance = int(movement[1:])

            if direction == 'R':
                for x in range(distance):
                    wires[wireId].append((wires[wireId][-1][0] + 1,wires[wireId][-1][1]))
            elif direction == 'L':
                for x in range(distance):
                    wires[wireId].append((wires[wireId][-1][0] - 1,wires[wireId][-1][1]))
            elif direction == 'U':
                for x in range(distance):
                    wires[wireId].append((wires[wireId][-1][0],wires[wireId][-1][1] + 1))
            elif direction == 'D':
                for x in range(distance):
                    wires[wireId].append((wires[wireId][-1][0],wires[wireId][-1][1] - 1))

        wireId += 1

    intersections = []
    for k1,v1 in wires.items():
        for k2,v2 in wires.items():
            if k1 != k2:
                a = set(v1)
                b = set(v2)
                if(a & b):
                    intersections.append(list(a & b))

    s = set()
    for inter in intersections:
        for pos in inter:
            if pos != (0,0):
                s.add(pos)

    distances = []
    for x in list(s):
        distances.append(abs(x[0]) + abs(x[1]))
    
    print(min(distances))
