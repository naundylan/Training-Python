from math import *

x, k = map(float, input().split())
c = sqrt(abs(x))
a = pow(c, 4) + pow(k, 3)
f = pow(log10(a), 3) + pow(cos(x), 5)

print('%.2f' %f)