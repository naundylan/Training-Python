def matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"nhap hang {i + 1}: ").split()))
        while len(row) != cols:
            print(f"vui long nhap dung {rows} phan tu")
            row = list(map(int, input(f"nhap hang {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def sum_matrix(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols)] for i in range(rows)]
    return result

if __name__ == "__main__":
    print("nhap kich thuoc n, m: ", end="")
    rows, cols = map(int, input().split())
    a = matrix(rows, cols)
    b = matrix(rows, cols)
    c = sum_matrix(a, b)
    print("tong cua hai ma tran la: ", c)