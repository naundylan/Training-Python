a, b, c = map(int, input().split())

if a + b > c and a + c > b and c + b > a and a > 0 and b > 0 and c > 0:
    if a == b and a == c and c == b:
        print(1)

    elif a == b and a != c:
        print(2)

    elif a ** 2 + b ** 2 == c ** 2 or b * b == a * a + c * c or c * c + b * b == a * a:
        print(3)

    else:
        print(4) 
else:
    print("INVALID")