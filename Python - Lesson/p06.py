n = input()

upper = 0
lower = 0
digit = 0
other = 0

for i in n:
    if i.isalpha():
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1
print(upper, lower, digit, other)