# 13246

def mul(a, b, n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= 1000
    return res


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
my_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

while b:
    if b % 2:
        my_matrix = mul(my_matrix, matrix, n)
    b >>= 1
    matrix = mul(matrix, matrix, n)

for i in my_matrix:
    print(*i)
