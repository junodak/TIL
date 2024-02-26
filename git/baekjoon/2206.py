from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

def bfs(i, j):
    while True:
        pass

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j] = 0
            dq = deque()
            bfs(0, 0)
            arr[i][j] = 1