def inData():
    male, female = 0, 0
    students = []
    n = int(input())
    for i in range(n):
        line = input().split(";")
        if line[2] == " M":
            male += 1
        elif line[2] == " F":
            female += 1
        students.append(line)
    print(male, female)

    students.sort(key = lambda x : x[3])
    for i in students:
        print(";".join(i))
inData()