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

    intersections = list(s)
    distances = defaultdict(int)
    for k,v in wires.items():
        counter = 0
        for pos in v:
            if pos in intersections: # Posible checkear repeticion de entradas
                distances[str(pos[0]) + str(pos[1])] += counter

            counter += 1

    print('Fewer Steps: {}'.format(min([v for k,v in distances.items()])))
    
