# import heapq
# q = []
# v, e = map(int, input().split())
#
# # 그래프 생성
# arr = [[0]*v for _ in range(v)]
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     arr[a-1][b-1] = c
#     arr[b-1][a-1] = c
#
# # 초기값 : 첫번째 정점의 간선 힙큐에 추가
# visited = [1] + [0]*(v-1)
# for i in range(v):
#     if arr[0][i]:
#         heapq.heappush(q, (arr[0][i], 0, i))
#
# total_weight = 0
# while q:
#     weight, x, y = heapq.heappop(q)
#     if visited[x] == 1 and visited[y] == 1:
#         continue
#     total_weight += weight
#     visited[y] = 1
#     for i in range(v):
#         if arr[y][i] and visited[i] == 0:
#             heapq.heappush(q, (arr[y][i], y, i))
# print(total_weight)

import heapq
q = []
v, e = map(int, input().split())

# 그래프 생성
arr = [[] for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a-1].append((c, a-1, b-1))
    arr[b-1].append((c, b-1, a-1))

# 초기값 : 첫번째 정점의 간선 힙큐에 추가
visited = [1] + [0]*(v-1)
for i in arr[0]:
    heapq.heappush(q, i)

res = 0
while q:
    w, x, y = heapq.heappop(q)
    if visited[y] == 0:
        visited[y] = 1
        res += w
        for i in arr[y]:
            heapq.heappush(q, i)
print(res)