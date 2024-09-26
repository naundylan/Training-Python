n, m, a = map(int, input().split())
x, y = 0, 0
if n % a == 0:
    x = n // a
else:
    x = n // a + 1
if m % a == 0:
    y = m // a
else:
    y = m // a + 1
print(x * y)