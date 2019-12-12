from collections import defaultdict
import itertools

def count(digit,numbers):
    count = 0
    for i in numbers:
        if i == digit:
            count += 1
    return count

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

    selectedLayer = 0
    zeros = 999999999999
    for k,v in layers.items():
        if count(0,sum(v,[])) < zeros:
            zeros = count(0,sum(v,[]))
            selectedLayer = k

    ones = count(1,sum(layers[selectedLayer],[]))
    twos = count(2,sum(layers[selectedLayer],[]))

    print('Layer {} --> Number of 1s = {} * Number of 2s = {} --> {}'.format(selectedLayer,ones,twos,int(ones*twos)))
   