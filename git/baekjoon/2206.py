from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)] # 0000 들어온걸 [0,0,0,0] 으로 저장

dn = [1, -1, 0, 0]  # 상하좌우 델타
dm = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0))                                            # (0, 0) 에서 시작
    visited = [[0]*m for _ in range(n)]                         # visited
    visited[0][0] = 1                                           # (0, 0) 1번째로 방문
    while q:
        qi, qj = q.popleft()
        for k in range(4):
            di = qi + dn[k]
            dj = qj + dm[k]
            if 0 <= di < n and 0 <= dj < m:                     # 상하좌우 갈 수 있으면 각각 append
                if arr[di][dj] == 0 and visited[di][dj] == 0:
                    q.append((di, dj))
                    visited[di][dj] += visited[qi][qj] + 1      # visited에 최단거리 저장
        if visited[n-1][m-1] != 0:                              # 마지막 칸에 갔으면
            path.append(visited[n-1][m-1])                      # 최단거리 추가
            break                                               # bfs 종료

path = []
for i in range(n):
    for j in range(m):
        bfs()                       # 벽 안부수고 최단거리
        if arr[i][j]:               # 벽 있다면
            cnt = 0
            for k in range(4):      # 벽 상하좌우에 벽이 몇개 있는지 세서 부술 가치 판단
                di = i+dn[k]
                dj = j+dm[k]
                if 0 <= di < n and 0 <= dj < m and arr[di][dj]==0:
                    cnt += 1
            if cnt >= 2:            # 부술 가치가 있다면
                arr[i][j] = 0       # 부수고
                bfs()               # 최단거리
                arr[i][j] = 1       # 다시 복구
if path == []:
    print(-1)                       # 최단거리 추가된 적이 없다면 -1
else:
    print(min(path))                # 최단거리중 가장 짧은거로