from math import *
x = float(input())

if x == -3:
    print("Div by zero")
elif x > 0:
    print('%.6f' %(x*x + sqrt(x) + 1))
else:
    print('%.6f' %((x**3 + 2*x + 1)/(x + 3)))