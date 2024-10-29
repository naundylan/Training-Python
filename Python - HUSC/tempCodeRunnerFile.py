from math import *
x = float(input())
sum = 1.0
i = 1
tmp = 1.0
while abs(tmp) >= pow(10, -9):
    tmp = x**i / factorial(i)
    sum += tmp
    i+=1
print('%.4f' % sum)
