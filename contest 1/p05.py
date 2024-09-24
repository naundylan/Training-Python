from math import *

x1, y1, x2, y2 = map(int, input().split())

print('%.2f' % (sqrt(int(pow(x2 - x1, 2)) + int(pow(y2 - y1, 2)))))