def final1(n):
    result = n.split()
    return result[-1]
def final2(n):
    index = n.rfind(" ")
    result = n[index + 1:]
    return result
if __name__ == "__main__":
    n = input()
    print(final1(n))
    print(final2(n))