n = int(input())

ans = n // 28
vo = ans
while vo >= 3:
    tmp = vo // 3
    ans += tmp
    vo = vo % 3 + tmp
print(ans)