
with open('input.data','r') as f:
    group = [int(line) for line in f.readlines()]
    
    modules = [0] * len(group)
    totalFuel = 0

    counter = 0
    for mass in group:
        partialMass = mass
        while partialMass > 0:
            partialMass = int(int(partialMass) / 3) - 2
            if partialMass > 0:
                modules[0] += partialMass

    for x in modules:
        totalFuel += x

print("Total fuel = {}".format(totalFuel))