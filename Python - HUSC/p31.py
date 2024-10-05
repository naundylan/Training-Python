n = int(input())

cnt=0
ds = []
for i in range(1, n+1):
    if n % i == 0:
        cnt+=1
        ds.append(i)
print(cnt)
for i in ds:
    print(i, end=" ")