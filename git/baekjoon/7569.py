import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[[0]*m for _ in range(n)] for _ in range(h)]

cnt = 0
q = deque()
for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
            if arr[i][j][k] == 0:
                cnt += 1

max = 0
while q:
    i, j, k = q.popleft()
    if max < arr[i][j][k]:
        max = arr[i][j][k]

    if i-1 >= 0 and arr[i-1][j][k] == 0:
        q.append((i-1, j, k))
        arr[i-1][j][k] = arr[i][j][k] + 1
        cnt -= 1
    if i+1 < h and arr[i+1][j][k] == 0:
        q.append((i+1, j, k))
        arr[i+1][j][k] = arr[i][j][k] + 1
        cnt -= 1
    if j-1 >= 0 and arr[i][j-1][k] == 0:
        q.append((i, j-1, k))
        arr[i][j-1][k] = arr[i][j][k] + 1
        cnt -= 1
    if j+1 < n and arr[i][j+1][k] == 0:
        q.append((i, j+1, k))
        arr[i][j+1][k] = arr[i][j][k] + 1
        cnt -= 1
    if k-1 >= 0 and arr[i][j][k-1] == 0:
        q.append((i, j, k-1))
        arr[i][j][k-1] = arr[i][j][k] + 1
        cnt -= 1
    if k+1 < m and arr[i][j][k+1] == 0:
        q.append((i, j, k+1))
        arr[i][j][k+1] = arr[i][j][k] + 1
        cnt -= 1

if cnt:
    print(-1)
else:
    print(max-1)