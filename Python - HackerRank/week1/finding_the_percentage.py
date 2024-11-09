def average(student_marks, name):
    sum = 0.0
    for i in student_marks[name]:
        sum += i
    return sum / 3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = average(student_marks, query_name)
    print("%.2f" % (result))