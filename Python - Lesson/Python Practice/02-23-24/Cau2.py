def check(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i] and i != j:
                return True
    return False
if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    if check(matrix, n):
        print("Do thi co huong")
    else:
        print("Do thi vo huong")
    