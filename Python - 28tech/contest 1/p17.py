c = input()

if c.islower():
    print("LOWER")
elif c.isdigit():
    print("DIGIT")
elif c.isupper():
    print("UPPER")
else:
    print("SPECIAL")