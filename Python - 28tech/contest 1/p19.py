m, n = map(int, input().split())

if n % 2 == 0:
    print(n // 2 * m)
else:
    print((n - 1) // 2 * m + m // 2)