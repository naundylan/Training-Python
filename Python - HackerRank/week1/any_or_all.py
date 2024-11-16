def palindromicNum(num):
    m = num
    x = 0
    while(m != 0):
        x = x*10 + m%10
        m = m // 10
    return x == num
if __name__ == "__main__":
    n = int(input())
    list = list(map(int, input().split()))
    if all(num >= 0 for num in list):
        if any(palindromicNum(num) == True for num in list):
            print(True)
        else:
            print(False)
    else:
        print(False)
    