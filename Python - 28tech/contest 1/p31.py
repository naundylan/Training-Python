from math import *

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())

cup = a1 + a2 + a3
hc = b1 + b2 + b3

ke1, ke2 = 0, 0

if cup % 5 == 0:
    ke1 = cup // 5
else:
    ke1 = cup // 5 + 1

if hc % 10 == 0:
    ke2 = hc // 10
else:
    ke2 = hc // 10 + 1

if ke1 + ke2 <= n:
    print("YES")
else:
    print("NO")