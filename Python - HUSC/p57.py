from math import *
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    s, v = 0, 0
    max = a[s]
    min = a[s]
    for i in range(0, n + 1):
        if a[i] > max:
            max = a[i]
            s = i
        if a[i] < min:
            min = a[i]
            v = i
    print(abs(max - min))