from math import *
a, b, c = map(float, input().split())

if abs(a-b)<=0.000000001 and abs(a-c)<=0.000000001 and abs(b-c)<=0.000000001:
    print("Tam giac deu")
elif abs(a-b)<=0.000000001 or abs(a-c)<=0.000000001 or abs(b-c)<=0.000000001:
    print("Tam giac can")
else:
    print("Tam giac thuong")