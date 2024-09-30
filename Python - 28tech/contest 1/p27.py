from math import *
a = float(input())

if a - int(a) >= 0.5:
    print(ceil(a))
else:
    print(int(a))