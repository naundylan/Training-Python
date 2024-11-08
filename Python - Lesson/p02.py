def filt(n):
    new = []
    for i in range(len(n)):
        if i % 2 != 0:
            new.append(i)
    return new
if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(filt(n))