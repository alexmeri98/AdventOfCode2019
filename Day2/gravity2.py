with open('input.data','r') as f:
    intcode = list(map(int,(f.readline()).split(',')))
    noun = 0
    verb = 0
    for x in range(0,100):
        for y in range(0,100):
            copyIntcode = intcode[:]
            copyIntcode[1] = x
            copyIntcode[2] = y

            i = 0 
            halt = False
            while halt == False:
                if(copyIntcode[i] == 1):
                    copyIntcode[copyIntcode[i + 3]] = copyIntcode[copyIntcode[i + 1]] + copyIntcode[copyIntcode[i + 2]]
                elif(copyIntcode[i] == 2):
                    copyIntcode[copyIntcode[i + 3]] = copyIntcode[copyIntcode[i + 1]] * copyIntcode[copyIntcode[i + 2]]
                elif(copyIntcode[i] == 99):
                    halt = True
                i += 4

            if(copyIntcode[0] == 19690720):
                noun = x
                verb = y
                break
    print("Inputs noun {} and verb {} --> {}".format(noun,verb,(100 * noun + verb)))