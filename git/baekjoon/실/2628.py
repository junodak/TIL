n, m = map(int, input().split())

num = int(input())
arr = [[0],[0]]
for i in range(num):
    line, idx = map(int, input().split())
    arr[line].append(idx)
arr[0].append(m)
arr[1].append(n)

for i in range(2):
    if len(arr[i]) > 1:
        arr[i].sort()
        for j in range(len(arr[i])-1,-1,-1):
            arr[i][j] -= arr[i][j-1]
        arr[i][0] = 0

print(max(arr[0])*max(arr[1]))