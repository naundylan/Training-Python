t = int(input())

for i in range(t):
    a, b, c, d, tmp = map(int, input().split())
    p = max(a, b, c, d)
    cnt = 0
    if (a+b+c+d == 4*p or a+b+c+d+tmp == 4*p) and (a==b==c or a==c==d or b==c==d or a==b==d):
        print("Yes")
    else:
        print("No")