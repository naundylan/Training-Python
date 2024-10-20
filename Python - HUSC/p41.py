n = int(input())
kq = 0
for i in range(1, n+1):
    kq+=float(1/i)
print('%.6f' % kq)