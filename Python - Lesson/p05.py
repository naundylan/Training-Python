def remove(s):
    str = s[0]
    for j in range(0, len(s)-1):
        if s[j] != s[j+1]:
            str += s[j+1]
    return str
if __name__ == "__main__":
    n = input().split()
    for i in range(len(n)):
        n[i] = remove(n[i])
    print(" ".join(n))