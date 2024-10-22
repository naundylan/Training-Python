if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    tmp = min(arr)
    for item in arr:
        if item != m and item > tmp:
            tmp = item
    print(tmp)