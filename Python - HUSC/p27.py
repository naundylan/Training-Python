a, b, c, d = map(int, input().split())

print("%02d"%((a*b*c*d) % 100))