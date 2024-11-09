n = input()
result = ""
for i in range(-1, -len(n) - 1, -1):
    result += n[i]
if result == n:
    print("yes")
else:
    print("no")