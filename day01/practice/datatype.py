################ print(object, sep, end) ###############

# default
print('hello')
# sep = ',' & end = "hehe"
a = 10
b = 20
c = 30
print(a, b ,c ,sep = ',', end = "hehe")





################# comment in python ###############

# this is a comment in python
""" this is a paragraph in python
this line too"""
''' this type too'''




################# variable type ###############

one = 2
two = "hello"
three = True
print(type(two))
print(type(three))

# -> number type: int, float, complex number

x = 1
w = 11111111111111111111111111111111111111111111111111111111111111111111111111111 #very big int but its okay
y = 1.1
z = 1 + 2j
# int to hex, oct, bin
bin = 0b1101
print(bin) # bin = 13
oct = 0o123
print(oct) # oct = 83
hex = 0x22A
print(hex) # hex = 554

# -> float

f1 = 3.5
f2 = 3e5 #3*10^5
f3 = 1.9e308 #inf
f4 = 5.4e-325 #0.0
# float with round
m = 28.0412323
print(round(m, 2)) # 28.04 but it can round to int
print('%.2f' % m) #28.04
print('{:.2f}'.format(m)) #28.04

# -> complex num

num = 10 + 20j
print(num.real)
print(num.imag)

# -> bool type

print(bool(100)) # True
print(bool(0)) # False
print(bool('100')) # True
print(bool('')) # False

# -> string (no character type)

str = "namquyen"
print(str[0]) # n
print(str)
para = """this is a 
paragraph"""
print(para)

# -> casting (ép kiểu)
s = 123456
print(int(s + 1)) #123457
t = 123.123
print(int(t)) #123
v = "123aaa"
print(int(v)) #error