a, b = map(int, input().split())

if a == 0:
    if b == 0:
        print("Many Solutions")
    else:
        print("No Solution")
else:
    print('%.2f' %(-b/a))
