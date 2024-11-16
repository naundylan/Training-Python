def sorting(a):
    a.sort()
    upper = [up for up in a if up.isupper()]
    lower = [low for low in a if low.islower()]
    digit = [num for num in a if num.isdigit()]
    even = [num for num in digit if int(num) % 2 == 0]
    odd = [num for num in digit if int(num) % 2 != 0]
    return "".join(lower) + "".join(upper) + "".join(odd) + "".join(even)

if __name__ == "__main__":
    n = input()
    a = [item for item in n]
    print(sorting(a))
