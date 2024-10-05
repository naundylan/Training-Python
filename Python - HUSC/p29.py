n, m, k = map(int, input().split())

phong = 0

if n % k == 0:
    phong += n // k
else:
    phong += n // k + 1

if m % k == 0:
    phong += m // k
else:
    phong += m // k + 1

print(phong)