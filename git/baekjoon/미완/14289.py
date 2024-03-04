def mul(a, b, n):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += a[i][k]*b[k][j]
            r[i][j] %= 1000000007
    return r


n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1
    matrix[j-1][i-1] = 1

d = int(input())
my_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
while d:
    if d % 2:
        my_matrix = mul(my_matrix, matrix, n)
    matrix = mul(matrix, matrix, n)
    d >>= 1
print(my_matrix[0][0])
