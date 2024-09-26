a, b, c = map(int, input().split())

print(min(a + b + c, 2*(a + b), 2*(c + b), 2*(a + c)))
