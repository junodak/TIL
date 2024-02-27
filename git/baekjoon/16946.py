from collections import deque

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = group_num
    cnt = 0
    while q:
        qi, qj = q.popleft()
        cnt += 1
        for k in range(4):
            di = qi + dn[k]
            dj = qj + dm[k]
            if 0 <= di < n and 0 <= dj < m:
                if visited[di][dj] == 0 and arr[di][dj] == 0:
                    q.append((di, dj))
                    visited[di][dj] = group_num
    group_cnt.append(cnt)


n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
group_cnt = [0]
group_num = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == 0:
            group_num += 1
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            a = set()
            for k in range(4):
                dx = i + dn[k]
                dy = j + dm[k]
                if 0 <= dx < n and 0 <= dy < m:
                    a.add(visited[dx][dy])
            for k in a:
                arr[i][j] += group_cnt[k]
            arr[i][j] %= 10
        print(arr[i][j], end='')
    print()