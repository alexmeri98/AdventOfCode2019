password = 136818
numPasswords = 0
while password < 685979:
    neverDecrease = False
    adjacents = False
    analyze = str(password)
    for i in range(1,len(analyze)):
        if int(analyze[i]) == int(analyze[i - 1]):
            adjacents = True

        if int(analyze[i]) >= int(analyze[i - 1]):
            neverDecrease = True
        else:
            neverDecrease = False
            break
    
    if neverDecrease and adjacents:
        numPasswords += 1
    password += 1

print('Number of passwords: {}'.format(numPasswords))