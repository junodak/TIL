def mul(a, b, n):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += a[i][k]*b[k][j]
            r[i][j] %= 1000000007
    return r

matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

d = int(input())
bin_d = int(bin(d)[2:])
n = 8
my_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            my_matrix[i][j]=1

while bin_d:
    if bin_d%10:
        my_matrix = mul(my_matrix, matrix, n)
    matrix = mul(matrix, matrix, n)
    bin_d//=10
print(my_matrix[0][0])