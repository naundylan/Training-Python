h, a, b = map(int, input().split())
if(a <= b and a < h):
    print(-1)
else:
    day = 0
    tmp = 0
    while(tmp < h):
        tmp += a
        day += 1
        if tmp >= h:
            break
        tmp -= b
    print(day)