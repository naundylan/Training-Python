a, b = map(int, input().split())

if a % b == 0:
    print("Yes")
elif b % a == 0:
    print("Yes")
else:
    print("No")