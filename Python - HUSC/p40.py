def gt(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        kq = 1
        for i in range(2, n+1, 2):
            kq *= i
        return kq
    else:
        kq = 1
        for i in range(1, n+1, 2):
            kq *= i
        return kq
    
if __name__ == "__main__":
    n = int(input())
    print(gt(n))