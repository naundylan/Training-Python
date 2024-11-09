from itertools import product
if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    list = list(product(a, b))
    for i in list:
        print(i, end=" ")