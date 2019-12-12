from collections import defaultdict
import itertools

with open('input.data','r') as f:
    data = list(map(int,f.readline()))

    wide = 25
    tall = 6
    numOfLayers = int(len(data)/(wide * tall))

    layers = defaultdict(list)
    i = 0
    for num in range(numOfLayers):
        countTall = 0
        while countTall != tall:
            line = []
            countWide = 0
            while countWide != wide:
                line.append(data[i])
                i += 1
                countWide += 1
            layers[num + 1].append(line)
            countTall += 1
    
    for line in range(tall):
        for pixel in range(wide):
            value = layers[1][line][pixel]
            if value == 2:
                layer = 2
                newPixel = 2
                while newPixel == 2:
                    newPixel = layers[layer][line][pixel]
                    layer += 1
                layers[1][line][pixel] = newPixel

    print('Message obtained:')
    for line in layers[1]:
        for pixel in line:
            if pixel == 0:
                print(' ',end=" ")
            else:
                print('x',end=" ")
        print()