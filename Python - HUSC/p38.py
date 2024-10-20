m,n = map(int, input().split())

x = int(n/2 - m)
y = m-x

if x > 0 and y > 0:
    print("Ga =", y)
    print("Cho =", x)
else:
    print(-1)