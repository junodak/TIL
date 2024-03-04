mod = 10**9 + 7

def mul(a, b, n):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += a[i][k]*b[k][j]
            r[i][j] %= mod
    return r


n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

my_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
while k:
    if k % 2:
        my_matrix = mul(my_matrix, matrix, n)
    matrix = mul(matrix, matrix, n)
    k >>= 1

sum = 0
print()
for i in my_matrix:
    print(*i)
    for j in i:
        sum += j
print(sum % mod)