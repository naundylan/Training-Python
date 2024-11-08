if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    tmp = [x for x in a if x % 2 == 0 or (x < 0 and x % 3 == 0)]
    print(len(tmp))