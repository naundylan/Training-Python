n, p, q = map(int, input().split())

for i in range(min(p,q), n+1):
    if i % q == 0 or i % p == 0:
        print(i, end=" ")