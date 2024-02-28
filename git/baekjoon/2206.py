from collections import deque

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0] = 1
q = deque()
q.append((0, 0, 0))
r = -1
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    i, j, w = q.popleft()
    if i==n-1 and j ==m-1:
        r = v[i][j][w]
        break
    for dn, dm in d:
        di, dj = i + dn, j + dm
        if 0 <= di < n and 0 <= dj < m and v[di][dj][w] == 0:
            if arr[di][dj] == '0':
                    q.append((di, dj, w))
                    v[di][dj][w] = v[i][j][w] + 1
            if arr[di][dj] == '1' and w == 0:
                    q.append((di, dj, 1))
                    v[di][dj][1] = v[i][j][w] + 1
print(r)



from collections import deque
A, B = map(int, input().split())
map = [input() for _ in range(A)]

answer = -1

que = deque()
que.append((0, 0, 1))

visited = [[[0, 0] for _ in range(B)] for _ in range(A)]
visited[0][0][1] = 1
DR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while que:
  p, q, r = que.popleft()
  v = visited[q][p][r]
  if p == B-1 and q == A-1:
    answer = v
    break
  for s, t in DR:
    x = p + s
    y = q + t
    if 0 <= x < B and 0 <= y < A:
      if map[y][x] == "1" and r:
        visited[y][x][0] = v + 1
        que.append((x, y, 0))
      elif map[y][x] == "0" and not visited[y][x][r]:
        visited[y][x][r] = v + 1 
        que.append((x, y, r))

print(answer)