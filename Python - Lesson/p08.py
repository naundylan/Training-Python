n = input().split(';')
tong = 0
for i in n:
    monhoc, diem = i.split('=')
    tong += int(diem)
print(tong)
