n = int(input())
tmp = n
tong = 0
while(tmp != 0):
    tong += tmp % 10
    tmp //= 10
if n % tong == 0:
    print("Yes")
else:
    print("No")