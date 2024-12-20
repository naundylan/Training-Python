from math import *
def soluongdequy(n):
    if n == 0:
        return 0
    else:
        return n + soluong(n-1)
def soluong(n):
    dem = 0
    while(n > 0):
        dem += 1
        n //= 10
    return dem
def tohop(n, k):
    return factorial(n)/(factorial(k) * factorial(n-k))
def tohopdequy(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return tohopdequy(n-1, k-1) + tohopdequy(n-1, k)