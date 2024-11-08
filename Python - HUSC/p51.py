from math import *
n, p, m = map(float, input().split())
month = 0
while n < m:
    n = n*(1 + p/100)
    month += 1
print(month)