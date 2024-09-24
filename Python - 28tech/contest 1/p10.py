a, b, c = map(int, input().split())

if a > 0 and b > 0 and c > 0 and a+b>c and b+c>a and c+a>b:
    print("YES")
else:
    print("NO")