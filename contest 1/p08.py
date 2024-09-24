x, y = map(int, input().split())

print(x + y)
print(x - y)
print(x * y)
if(x == 0 or y == 0):
    print("INVALID")
else:
    print('%.4f' % (x / y))