n = input()

li = list(map(int, list(n)))
tich = 1
tong = 0
for i in li:
    tich *= i
    tong += i
print('%.3f' % (tich/tong))