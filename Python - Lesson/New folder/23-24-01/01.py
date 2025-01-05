
def chuanhoa(x, newMin=0, newMax=1):
    newX = []
    for i in range(len(x)):
        newItem = (x[i] - min(x))/(max(x) - min(x))*(newMax - newMin) + newMin
        print(newItem)
        newX.append(newItem)
    return newX

print(chuanhoa([6,3,9,8,7], -1, 1))