from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

q = deque()
q.append(1)
cnt = 0
visited = [0]*(n+1)
visited[1] = 1
while q:
    len_q = len(q)
    min_q = min(q)
    for _ in range(len_q):
        x = q.popleft()
        for i in arr:
            if i[0] == x and visited[i[1]] == 0:
                q.append(i[1])
                visited[i[1]] = 1
            elif i[1] == x and visited[i[0]] == 0:
                q.append(i[0])
                visited[i[0]] = 1
    cnt += 1
print(min_q, cnt-1, len_q)