def mul(a, b, n):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += a[i][k]*b[k][j]
            r[i][j] %= 1000
    return r

n, b = map(int, input().split())
bin_b = int(bin(b)[2:])
matrix = [list(map(int, input().split())) for _ in range(n)]
my_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            my_matrix[i][j]=1
while bin_b:
    if bin_b%10:
        my_matrix = mul(my_matrix, matrix, n)
    matrix = mul(matrix, matrix, n)
    bin_b//=10

for i in my_matrix:
    print(*i)