with open('input.data','r') as f:
    intcode = list(map(int,(f.readline()).split(',')))
    intcode[1] = 12
    intcode[2] = 2

    i = 0 
    halt = False
    while halt == False:
        if(intcode[i] == 1):
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        elif(intcode[i] == 2):
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        elif(intcode[i] == 99):
            halt = True
        i += 4

    print(intcode[0])