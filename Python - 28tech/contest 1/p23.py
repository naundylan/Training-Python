n, m = map(int, input().split())

mi, ma = 0, n
if n % 2 == 0:
    mi = n // 2
else:
    mi = n // 2 + 1

ans = (mi + m - 1) // m * m
if ans <= ma:
    print(ans)
else:
    print(-1)