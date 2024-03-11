def mul(a, b):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= m
    return res

while True:
    n, m, p = map(int, input().split())
    if n+m+p == 0:
        break
    
    matrix = [list(map(int, input().split())) for i in range(n)]
    my_matrix = [[1 if i==j else 0 for i in range(n)] for j in range(n)]

    while p:
        if p%2:
            my_matrix = mul(my_matrix, matrix)
        matrix = mul(matrix, matrix)
        p >>= 1
    
    for i in my_matrix:
        print(*i)