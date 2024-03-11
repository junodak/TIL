import sys
input = sys.stdin.readline
print = sys.stdout.write


def mul(a, b):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k]*b[k][j] == 1:
                    res[i][j] = 1
                    break
    return res


n, k, m = map(int, input().split())

matrix = [[0]*n for _ in range(n)]
for i in range(n):
    p1, p2 = map(int, input().split())
    matrix[i][p1-1] = 1
    matrix[i][p2-1] = 1

my_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
while k:
    if k % 2:
        my_matrix = mul(my_matrix, matrix)
    matrix = mul(matrix, matrix)
    k >>= 1

for i in range(m):
    p1, p2 = map(int, input().split())
    if my_matrix[p1-1][p2-1]:
        print('death\n')
    else:
        print('life\n')
