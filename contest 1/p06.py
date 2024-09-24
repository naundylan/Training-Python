n = int(input())

if n % 2 == 0:
    print("YES")
else:
    print("NO")

if n % 3 == 0 and n % 5 == 0:
    print("YES")
else:
    print("NO")

if n % 3 == 0 and n % 7 != 0:
    print("YES")
else:
    print("NO")

if n % 3 == 0 or n % 7 == 0:
    print("YES")
else:
    print("NO")

if n > 30 and n < 50:
    print("YES")
else:
    print("NO")

if n >= 30 and (n % 5 == 0 or n % 3 == 0 or n % 2 == 0):
    print("YES")
else:
    print("NO")

r = n % 10
if (r >= 10 and r <= 99) and (r == 2 or r == 7 or r == 3 or r == 5):
    print("YES")
else:
    print("NO")

if n <= 100 and n % 23 == 0:
    print("YES")
else:
    print("NO")

if n < 10 and n > 20:
    print("YES")
else:
    print("NO")

if r % 3 == 0:
    print("YES")
else:
    print("NO")    