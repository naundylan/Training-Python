l1, r1, l2, r2 = map(int, input().split())

if l1 <= r2 and l2 <= r1:
    dau=max(l1, l2)
    cuoi=min(r1, r2)
    print(dau, cuoi)
else:
    print(-1)