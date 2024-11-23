if __name__ == "__main__":
    n, m = map(int, input().split())
    line = "---"
    tmp = ".|."
    str = "WELCOME"

    # top mat
    for i in range(n//2):
        print((tmp*i + tmp + tmp*i).center(m, '-'))

    # middle mat
    print(str.center(m, '-'))

    # bottom mat
    for i in range(n//2):
        print((tmp*(n//2 - i - 1) + tmp + tmp*(n//2 - i - 1)).center(m, '-'))