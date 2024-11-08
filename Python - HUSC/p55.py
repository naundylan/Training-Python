if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = max(a)
    print(sum([x for x in a if x != b]))