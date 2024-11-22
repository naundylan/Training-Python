def swap_case(str):
    tmp = ""
    for c in str:
        if c.isupper():
           tmp += c.lower() 
        elif c.islower():
            tmp += c.upper()
        else:
            tmp += c
    return tmp
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) 