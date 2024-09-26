n, a, b = map(int, input().split())

if a > b:
    if n % 2 == 0:
        print(n // 2 * b)
    else:
        print((n - 1) // 2 * b)
elif a <= b:
    print(n * a)