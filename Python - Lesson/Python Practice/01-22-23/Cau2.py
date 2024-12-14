str = input()
cnt = 0
for i in range(len(str) - 1):
    if (str[i].isdigit() and not str[i + 1].isdigit()) or (i == len(str) - 2 and str[i].isdigit()):
        cnt += 1
print(cnt)