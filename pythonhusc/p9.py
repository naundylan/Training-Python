from math import *

x1, y1, x2, y2 = map(int, input().split())

gap = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print('%.9f' %gap)