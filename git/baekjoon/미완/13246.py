import sys
input = sys.stdin.readline

def mat_add(a, b):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = (a[i][j] + b[i][j]) % mod
    return res


def mat_sub(a, b):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = (a[i][j] - b[i][j]) % mod
    return res


def mat_mul(a, b):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k]*b[k][j]
                res[i][j] %= mod
    return res


def mat_pow(a, b):
    res = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while b:
        if b % 2:
            res = mat_mul(res, a)
        a = mat_mul(a, a)
        b >>= 1
    return res


def solution(a, b):
    if b == 1:
        return mat_add(I, a)
    elif b % 2:
        return mat_mul(mat_add(I, a), solution(mat_pow(a, 2), b//2))
    else:
        return mat_add(solution(a, b-1), mat_pow(a, b))


mod = 1000
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in [0]*n]
I = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
R = mat_sub(solution(a, b), I)
for i in R:
    print(*i)
