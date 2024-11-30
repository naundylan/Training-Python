def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"nhap hang {i + 1}:").split()))
        while len(row) != rows:
            print(f"vui long nhap dung {rows} phan tu")
            row = list(map(int, input(f"nhap hang {i + 1}:").split()))
        matrix.append(row)
    return matrix

def main_diagonal()

def multi_matrix(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    matrix_c = [[0] * cols] * rows
    for i in range(rows):
        for j in range(cols):
            matrix_c[i][j] = matrix_a[i][j] * matrix_b[j][i]
    return matrix_c

if __name__ == "__main__":
    print("nhap kich thuoc n, m: ", end="")
    rows, cols = map(int, input().split())
    a = input_matrix(rows, cols)
    b = input_matrix(rows, cols)
    c = multi_matrix(a, b)
    print("ma tran tich la: ", c)
