from math import *
def uocso(n):
    tong = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong - n
n = int(input())
if uocso(n) > n:
    print(uocso(n))