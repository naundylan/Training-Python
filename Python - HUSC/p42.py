from math import *
n = int(input())
tong = 1
for i in range(2, isqrt(n) + 1):
    if n % i == 0:
        tong += i + (n//i)
if tong > n:
    print("YES")
else:
    print("NO")