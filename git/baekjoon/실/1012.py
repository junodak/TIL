import sys
input = sys.stdin.readline

def find_one(i, j):
    arr[i][j] = 0
    if i-1 >= 0 and arr[i-1][j]:   # 상
        find_one(i-1, j)  # 범위를 벗어나지 않고, 값이 1이면 재귀
    if i+1 < n and arr[i+1][j]:    # 하
        find_one(i+1, j)
    if j-1 >= 0 and arr[i][j-1]:   # 좌
        find_one(i, j-1)
    if j+1 < m and arr[i][j+1]:    # 우
        find_one(i, j+1)

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    sys.setrecursionlimit(n*m+1)   # 재귀 limit 늘려주기
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt += 1
                find_one(i, j)
    print(cnt)