def swap_case(s):
    for i in  range(s.len()):
        if s[i].isupper():
            s[i] = s[i].lower()
        elif s[i].islower():
            s[i] = s[i].upper()
	return s
if __name__ == '__main__':
    str = input()
    print(swap_case(str))