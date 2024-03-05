import heapq
q = []
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
arr = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist = ((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5
        arr[i][j] = dist
        arr[j][i] = dist

# 초기값 : 첫번째 정점의 간선 힙큐에 추가
visited = [1] + [0]*(n-1)
for i in range(n):
    if arr[0][i]:
        heapq.heappush(q, (arr[0][i], 0, i))

total_weight = 0
while q:
    weight, x, y = heapq.heappop(q)
    if visited[x] == 1 and visited[y] == 1:
        continue
    total_weight += weight
    visited[y] = 1
    for i in range(n):
        if arr[y][i] and visited[i] == 0:
            heapq.heappush(q, (arr[y][i], y, i))
print(round(total_weight, 2))





#     a, b, c = map(int, input().split())
#     arr[a-1].append((c, a-1, b-1))
#     arr[b-1].append((c, b-1, a-1))
#
# visited = [1] + [0]*(v-1)
# for i in arr[0]:
#     heapq.heappush(q, i)
#
# res = 0
# while q:
#     w, x, y = heapq.heappop(q)
#     if visited[y] == 0:
#         visited[y] = 1
#         res += w
#         for i in arr[y]:
#             if visited[i[2]] == 0:
#                 heapq.heappush(q, i)
# print(res)