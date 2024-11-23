def check(string):
    a = [False] * 5
    for c in string:
        if c.isalnum():
            a[0] = True
        if c.isalpha():
            a[1] = True
        if c.isdigit():
            a[2] = True
        if c.islower():
            a[3] = True
        if c.isupper():
            a[4] = True
    for tmp in a:
        print(tmp)
if __name__ == '__main__':
    s = input()
    check(s)