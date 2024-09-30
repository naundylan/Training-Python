a, b, c, x, y = map(int, input().split())

if ((a<=x and b<=y)or(b<=x and a<=y)) or ((a<=x and c<=y)or(c<=x and a<=y)) or ((b<=x and c<=y)or(c<=x and b<=y)):
    print("Yes")
else:
    print("No")