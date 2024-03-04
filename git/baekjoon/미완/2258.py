import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n줄, 필요한무게 m
arr = [list(map(int, input().split())) for _ in range(n)] # [무게, 가격] * n

# 가격이 싼 순서대로 먼저 나열, 가격이 같다면 무게가 높은순
print(arr)
arr.sort(key=lambda x : (x[1], -x[0]))
print(arr)
# 가격이 같다면 비용도 증가
for i in range(1, n):
    arr[i][0] += arr[i-1][0]
print(arr)
l, r = 0, 1
while r < n:
    if arr[l][1] == arr[r][1]:
        arr[r][1] += arr[r-1][1]
        r += 1
    else:
        l = r
        r += 1
print(arr)
arr.sort(key=lambda x : (x[1], -x[0]))
print(arr)

cost = -1
for i in arr:
    if i[0] >= m:
        cost = i[1]
        break
print(cost)