from math import *

def prime_factorization(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                print(i, end=" ")
                n //= i
    if n > 1:
        print(n)

if __name__ == '__main__':
    n = int(input())
    prime_factorization(n)