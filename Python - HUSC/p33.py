n = int(input())
x = 0
m = n
while(m != 0):
    x = x*10 + m%10
    m = m // 10
if x == n:
    print("Yes")
else:
    print("No")