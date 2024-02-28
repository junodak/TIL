# from collections import deque

# def bfs():
#     d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     while q:
#         i, j, w = q.popleft()

#         if i==n-1 and j ==m-1:
#             return v[i][j][w]

#         for dn, dm in d:
#             di, dj = i + dn, j + dm
#             if 0 <= di < n and 0 <= dj < m and v[di][dj][w] == 0:
#                 if arr[di][dj] == 0:
#                         q.append((di, dj, w))
#                         v[di][dj][w] = v[i][j][w] + 1
#                 if arr[di][dj] == 1 and w < k:
#                         q.append((di, dj, w+1))
#                         v[di][dj][w+1] = v[i][j][w] + 1
#     return -1

# n, m, k = map(int, input().split())
# arr = [list(map(int, list(input()))) for _ in range(n)]
# v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
# v[0][0][0] = 1
# q = deque()
# q.append((0, 0, 0))
# print(bfs())




from collections import deque

n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
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
            if arr[di][dj] == '1' and w < k:
                    q.append((di, dj, w+1))
                    v[di][dj][w+1] = v[i][j][w] + 1
print(r)