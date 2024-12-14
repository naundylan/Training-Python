m, n, x, y = map(int, input().split())
print(m, n , x, y)
matrix = []
for i in range(m):
    tmp = list(map(int, input().split()))
    print(tmp)
    matrix.append(tmp)
command = input()
robot = matrix[x][y]
while command != "FINISH":
    if command == "RIGHT":
        y = y + 1
        robot += matrix[x][y]
    elif command == "LEFT":
        y = y - 1
        robot += matrix[x][y]
    elif command == "DOWN":
        x = x + 1
        robot += matrix[x][y]
    elif command == "UP":
        x = x - 1
        robot += matrix[x][y]
    command = input()
print(robot)
