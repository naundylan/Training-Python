from math import *
def uocso(n):
    tong = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong > n
n = int(input())
for i in range(1, n + 1):
    if uocso(i):
        print(i)