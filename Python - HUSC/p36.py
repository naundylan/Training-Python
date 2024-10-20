n = int(input())

for i in range(1,201):
    for j in range(1,201):
        if n*(i + j) == i*j:
            print(i, j)