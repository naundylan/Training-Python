from math import *
def square(n):
    s = isqrt(n)
    return s * s == n

if __name__ == "__main__":
    cnt = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if square(i):
            cnt += 1
    print(cnt)
