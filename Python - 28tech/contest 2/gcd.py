from math import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input("Enter two integers: ").split())
    print(gcd(a, b))
    print(lcm(a, b))
    