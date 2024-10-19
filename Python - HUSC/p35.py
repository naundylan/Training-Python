c = input()
t = int(input())
li = list(map(int, input().split()))
for i in range(t):
    for j in range(li[i]):
        print(c,end="")
    print()