import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()
    if i-1 >= 0 and arr[i-1][j] == 0:
        q.append((i-1, j))
        arr[i-1][j] = arr[i][j] + 1
    if i+1 < n and arr[i+1][j] == 0:
        q.append((i+1, j))
        arr[i+1][j] = arr[i][j] + 1
    if j-1 >= 0 and arr[i][j-1] == 0:
        q.append((i, j-1))
        arr[i][j-1] = arr[i][j] + 1
    if j+1 < m and arr[i][j+1] == 0:
        q.append((i, j+1))
        arr[i][j+1] = arr[i][j] + 1

max = 0
check = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            check = True
        if max < arr[i][j]:
            max = arr[i][j]
if check:
    print(-1)
else:
    print(max-1)