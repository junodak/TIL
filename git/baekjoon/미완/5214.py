# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
# arr = [list(map(int, input().split())) for _ in range(m)]
#
# q = deque()
# q.append(0)
# visited = [1]+[0]*n
# cnt = 0
# while q:
#     x = q.popleft()
#     for i in arr:
#         if i[0]-1 == x and visited[i[1]-1] == 0:
#             visited[i[1]-1] = 1
#             q.append(i[1]-1)
#             cnt += 1
#         elif i[1]-1 == x and visited[i[0]-1] == 0:
#             visited[i[0]-1] = 1
#             q.append(i[0]-1)
#             cnt += 1
# print(cnt)


n = int(input())
arr = {i+1:[i+1] for i in range(n)}
for _ in range(int(input())):
    a, b = map(int, input().split())
    c = list(set(arr[a] + arr[b]))
    for i in c:
        arr[i] = c
print(len(arr[1])-1)
