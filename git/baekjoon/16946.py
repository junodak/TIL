from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

zero = set()



for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            




# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [list(map(int, list(input().strip()))) for _ in range(n)]

# dn = [1, -1, 0, 0]
# dm = [0, 0, 1, -1]

# def bfs(i, j):
#     q = deque()
#     q.append((i, j))
#     visited = [[0]*m for _ in range(n)]
#     visited[i][j] = 1
#     cnt = 1
#     while q:
#         qi, qj = q.popleft()
#         for k in range(4):
#             di = qi + dn[k]
#             dj = qj + dm[k]
#             if 0 <= di < n and 0 <= dj < m:
#                 if arr[di][dj] == 0 and visited[di][dj] == 0:
#                     cnt += 1
#                     q.append((di, dj))
#                     visited[di][dj] = 1
#     return cnt%10

# path = []
# for i in range(n):
#     for j in range(m):
#         if arr[i][j]:
#             arr[i][j] = bfs(i, j)
#         print(arr[i][j], end='')
#     print()