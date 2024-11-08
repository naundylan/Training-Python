def check(n):
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return False
    return True

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(n)
    print(check(n))