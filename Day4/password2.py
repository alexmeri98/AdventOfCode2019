from collections import defaultdict

password = 136818
numPasswords = 0
while password < 685979:
    neverDecrease = False
    adjacents = False
    registryAdj = defaultdict()
    analyze = str(password)
    for i in range(1,len(analyze)):
        if int(analyze[i]) == int(analyze[i - 1]):
            adjacents = True
            if i == 1:
                registryAdj[(int(analyze[i - 1]))] = 1
                registryAdj[(int(analyze[i]))] += 1
            else:
                if (int(analyze[i])) not in registryAdj:
                    registryAdj[(int(analyze[i - 1]))] = 1
                    registryAdj[(int(analyze[i]))] += 1
                else:
                    registryAdj[(int(analyze[i]))] += 1

        if int(analyze[i]) >= int(analyze[i - 1]):
            neverDecrease = True
        else:
            neverDecrease = False
            break
    
    
    if neverDecrease:
        if len(registryAdj) == 1 and list(registryAdj.values())[0] > 2:
            adjacents = False

        if len(registryAdj) > 1:
            numAdj = 0
            for value in registryAdj.values():
                if value == 2:
                    numAdj += 1
            if numAdj >= 1:
                adjacents = True
            else:
                adjacents = False
        if adjacents:
            numPasswords += 1
    password += 1

print('Number of passwords: {}'.format(numPasswords))