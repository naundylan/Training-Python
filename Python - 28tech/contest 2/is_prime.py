def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(10))
    print(is_prime(20))
    print(is_prime(13))
    print(is_prime(100))
