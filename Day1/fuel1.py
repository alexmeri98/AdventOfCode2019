
with open('input.data','r') as f:
    group = f.readlines()
    
    totalFuel = 0
    for mass in group:
        totalFuel += int(int(mass) / 3) - 2

print("Total fuel = {}".format(totalFuel))