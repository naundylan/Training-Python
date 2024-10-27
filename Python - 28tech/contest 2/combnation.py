from math import *

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == '__name__':
    n, k = map(int, input("Enter two integers: ").split())
    print(comb(n, k))