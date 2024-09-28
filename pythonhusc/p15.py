from math import *
a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    p = (a + b + c)/2
    print('%.4f' %(sqrt(p*(p - a)*(p - b)*(p - c))))
else:
    print("No Solution")