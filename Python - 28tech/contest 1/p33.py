a, b, c, n = map(int, input().split())

if (a + b + c + n) % 3 == 0:
    tmp = (a + b + c + n) // 3
    if tmp >= a and tmp >= b and tmp >= c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")