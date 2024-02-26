import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while q:
        qi, qj = q.popleft()
        for k in range(4):
            di = qi + dn[k]
            dj = qj + dm[k]
            if 0 <= di < n and 0 <= dj < m:
                if arr[di][dj] == 0 and visited[di][dj] == 0:
                    q.append((di, dj))
                    visited[di][dj] += visited[qi][qj] + 1
    if visited[n-1][m-1] != 0:
        path.append(visited[n-1][m-1])

path = []
for i in range(n):
    for j in range(m):
        bfs()
        if arr[i][j]:
            cnt = 0
            for k in range(4):
                di = i+dn[k]
                dj = j+dm[k]
                if 0 <= di < n and 0 <= dj < m and arr[di][dj]==0:
                    cnt += 1
            if cnt >= 2:
                arr[i][j] = 0
                bfs()
                arr[i][j] = 1
if path == []:
    print(-1)
else:
    print(min(path))