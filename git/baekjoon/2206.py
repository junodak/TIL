from collections import deque
import sys
input = sys.stdin.readline

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

q = deque()
q.append((0, 0, False))
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
while q:
    qi, qj, wall_break = q.popleft()
    for k in range(4):
        di = qi + dn[k]
        dj = qj + dm[k]
        if 0 <= di < n and 0 <= dj < m:                     # 상하좌우 갈 수 있으면 각각 append
            if wall_break == False:
                if arr[di][dj] == 1 and visited[di][dj] == 0:
                    q.append((di, dj, True))
                    visited[di][dj] = visited[qi][dj] + 1

            if arr[di][dj] == 0 and visited[di][dj] == 0:
                q.append((di, dj, False))
                visited[di][dj] = visited[qi][qj] + 1       # visited에 최단거리 저장
            
if visited[n-1][m-1] != 0:                              # 마지막 칸에 갔으면
    print(visited[n-1][m-1])
else:
    print(-1)