from math import *
x = float(input())
sum = 0.0
i = 1
tmp = 1.0
while tmp >= 10e-9:
    sum += tmp
    tmp = tmp * x / i
    i+=1
print('%.4f' % sum)
