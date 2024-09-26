# A -> Z: 65 -> 90
# a -> z: 97 -> 122
# 0 -> 9: 48 -> 57

c = input()

if c == 'z' or c == 'Z':
    print('a')
else:
    print(chr(ord(c)+1).lower())