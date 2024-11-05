if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    am, duong, chan, le = 0, 0, 0, 0
    for _ in a:
        if _ % 2 == 0:
            chan += 1
        else:
            le += 1
        if _ > 0:
            duong += 1
        elif _ < 0:
            am += 1
print(am)
print(duong)
print(chan)
print(le)
