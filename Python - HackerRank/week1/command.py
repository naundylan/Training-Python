if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        command = input().split()
        if command[0] == "insert":
            numbers = list(map(int, command[1:]))
            a.insert(numbers[0], numbers[1])
        elif command[0] == "print":
            print(a)
        elif command[0] == "remove":
            number = int(command[1])
            a.remove(number)
        elif command[0] == "append":
            number = int(command[1])
            a.append(number)
        elif command[0] == "sort":
            a.sort()
        elif command[0] == "pop":
            a.pop()
        elif command[0] == "reverse":
            a.reverse()