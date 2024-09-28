from math import *

a, b, c = map(float, input().split())

delta = b*b - 4*a*c

if delta < 0:
    print("No Solution")
elif delta == 0:
    print('%.4f' %(-b/(2*a)))
else:
    print('%.4f' %((-b + sqrt(delta))/(2*a)))
    print('%.4f' %((-b - sqrt(delta))/(2*a)))