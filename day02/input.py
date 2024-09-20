############ input ##########

# -> string
m = input("nhap n: ")
print(m)

# -> number
n = int(input("nhap n: "))
print(n)

# -> multi number
s = input("nhap 3 so: ")
a = s.split()
x, y, z = map(int, a)
print(x+y+z)
# shorten
x, y, z, t = map(int, input().split())
print(x+y+z+t)
