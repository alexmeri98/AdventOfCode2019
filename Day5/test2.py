with open('input.data','r') as f:
    intcode = list(map(int,(f.readline()).split(',')))

    i = 0 
    halt = False
    while halt == False:
        opcode = intcode[i] if len(str(intcode[i])) == 1 else int(str(intcode[i])[-2:])
        parameter = str(intcode[i])[:-2] if len(str(intcode[i])) > 1 else ''

        if opcode == 1:

            if parameter != '':
                parameter = parameter.zfill(3)

                if parameter == '000':
                    intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
                elif parameter == '001':
                    intcode[intcode[i + 3]] = intcode[i + 1] + intcode[intcode[i + 2]]
                elif parameter == '010':
                    intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[i + 2]
                elif parameter == '011':
                    intcode[intcode[i + 3]] = intcode[i + 1] + intcode[i + 2]
                elif parameter == '100':
                    intcode[i + 3] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
                elif parameter == '101':
                    intcode[i + 3] = intcode[i + 1] + intcode[intcode[i + 2]]
                elif parameter == '110':
                    intcode[i + 3] = intcode[intcode[i + 1]] + intcode[i + 2]
                elif parameter == '111':
                    intcode[i + 3] = intcode[i + 1] + intcode[i + 2]
            else:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]

            i += 4
        elif  opcode == 2:

            if parameter != '':
                parameter = parameter.zfill(3)

                if parameter == '000':
                    intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
                elif parameter == '001':
                    intcode[intcode[i + 3]] = intcode[i + 1] * intcode[intcode[i + 2]]
                elif parameter == '010':
                    intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[i + 2]
                elif parameter == '011':
                    intcode[intcode[i + 3]] = intcode[i + 1] * intcode[i + 2]
                elif parameter == '100':
                    intcode[i + 3] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
                elif parameter == '101':
                    intcode[i + 3] = intcode[i + 1] * intcode[intcode[i + 2]]
                elif parameter == '110':
                    intcode[i + 3] = intcode[intcode[i + 1]] * intcode[i + 2]
                elif parameter == '111':
                    intcode[i + 3] = intcode[i + 1] * intcode[i + 2]
            else:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]

            i += 4
        elif  opcode == 3:

            print('Enter number:')
            num = input()

            if parameter != '':

                if parameter == '0':
                    intcode[intcode[i + 1]] = int(num)
                elif parameter == '1':
                    intcode[i + 1] = int(num)
            else:
                intcode[intcode[i + 1]] = int(num)

            i += 2
        elif  opcode == 4:

            if parameter != '':

                if parameter == '0':
                    print(intcode[intcode[i + 1]])
                elif parameter == '1':
                    print(intcode[i + 1])
            else:
                print(intcode[intcode[i + 1]])

            i += 2
        elif opcode == 5:
            if parameter != '':
                parameter = parameter.zfill(2)
                if parameter == '00':
                    if intcode[intcode[i + 1]] != 0:
                        i = intcode[intcode[i + 2]]
                    else:
                        i += 3
                elif parameter == '01':
                    if intcode[i + 1] != 0:
                        i = intcode[intcode[i + 2]]
                    else:
                        i += 3
                elif parameter == '10':
                    if intcode[intcode[i + 1]] != 0:
                        i = intcode[i + 2]
                    else:
                        i += 3
                elif parameter == '11':
                    if intcode[i + 1] != 0:
                        i = intcode[i + 2]
                    else:
                        i += 3
            else:
                if intcode[intcode[i + 1]] != 0:
                    i = intcode[intcode[i + 2]]
                else:
                    i += 3
        elif opcode == 6:
            if parameter != '':
                parameter = parameter.zfill(2)
                if parameter == '00':
                    if intcode[intcode[i + 1]] == 0:
                        i = intcode[intcode[i + 2]]
                    else:
                        i += 3
                elif parameter == '01':
                    if intcode[i + 1] == 0:
                        i = intcode[intcode[i + 2]]
                    else:
                        i += 3
                elif parameter == '10':
                    if intcode[intcode[i + 1]] == 0:
                        i = intcode[i + 2]
                    else:
                        i += 3
                elif parameter == '11':
                    if intcode[i + 1] == 0:
                        i = intcode[i + 2]
                    else:
                        i += 3
            else:
                if intcode[intcode[i + 1]] == 0:
                    i = intcode[intcode[i + 2]]
                else:
                    i += 3
        elif opcode == 7:
            if parameter != '':
                parameter = parameter.zfill(3)

                if parameter == '000':
                    if intcode[intcode[i + 1]] < intcode[intcode[i + 2]]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0                
                elif parameter == '001':
                    if intcode[i + 1] < intcode[intcode[i + 2]]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '010':
                    if intcode[intcode[i + 1]] < intcode[i + 2]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '011':
                    if intcode[i + 1] < intcode[i + 2]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '100':
                    if intcode[intcode[i + 1]] < intcode[intcode[i + 2]]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '101':
                    if intcode[i + 1] < intcode[intcode[i + 2]]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '110':
                    if intcode[intcode[i + 1]] < intcode[i + 2]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '111':
                    if intcode[i + 1] < intcode[i + 2]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
            else:
                if intcode[intcode[i + 1]] < intcode[intcode[i + 2]]:
                    intcode[intcode[i + 3]] = 1
                else:
                    intcode[intcode[i + 3]] = 0
            i += 4
        elif opcode == 8:
            if parameter != '':
                parameter = parameter.zfill(3)

                if parameter == '000':
                    if intcode[intcode[i + 1]] == intcode[intcode[i + 2]]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0                
                elif parameter == '001':
                    if intcode[i + 1] == intcode[intcode[i + 2]]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '010':
                    if intcode[intcode[i + 1]] == intcode[i + 2]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '011':
                    if intcode[i + 1] == intcode[i + 2]:
                        intcode[intcode[i + 3]] = 1
                    else:
                        intcode[intcode[i + 3]] = 0  
                elif parameter == '100':
                    if intcode[intcode[i + 1]] == intcode[intcode[i + 2]]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '101':
                    if intcode[i + 1] == intcode[intcode[i + 2]]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '110':
                    if intcode[intcode[i + 1]] == intcode[i + 2]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
                elif parameter == '111':
                    if intcode[i + 1] == intcode[i + 2]:
                        intcode[i + 3] = 1
                    else:
                        intcode[i + 3] = 0  
            else:
                if intcode[intcode[i + 1]] == intcode[intcode[i + 2]]:
                    intcode[intcode[i + 3]] = 1
                else:
                    intcode[intcode[i + 3]] = 0
            i += 4
        elif  opcode == 99:
            halt = True
