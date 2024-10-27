from math import *
def square(n):
    s = isqrt(n)
    return s * s == n

def cube(n):
    s = pow(n, 1/3)
    return s ** 3 == n

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    if square(n):
        print("YES")
    else:
        print("NO")
    
    if cube(n):
        print("YES")
    else:
        print("NO")