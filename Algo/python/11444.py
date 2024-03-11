def mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= 10**9
    return res


T = int(input())
for _ in range(T):
    matrix = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    n = int(input())
    while n:
        if n % 2:
            result = mul(result, matrix)
        matrix = mul(matrix, matrix)
        n >>= 1
    print(result[0][1])