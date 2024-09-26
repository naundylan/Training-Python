n = int(input())

year = n // 365
week = (n % 365) // 7
day = (n % 365) % 7

print(year, week, day)