n = int(input())
arr_max = []
arr_min = []
for i in range(n):
    a, b, c = map(int,input().split())
    arr_max.append([a, b, c])
    arr_min.append([a, b, c])

for i in range(n-2,-1,-1):
    arr_max[i][0] += max(arr_max[i+1][0], arr_max[i+1][1])
    arr_max[i][1] += max(arr_max[i+1][0], arr_max[i+1][1], arr_max[i+1][2])
    arr_max[i][2] += max(arr_max[i+1][1], arr_max[i+1][2])

for i in range(n-2,-1,-1):
    arr_min[i][0] += min(arr_min[i+1][0], arr_min[i+1][1])
    arr_min[i][1] += min(arr_min[i+1][0], arr_min[i+1][1], arr_min[i+1][2])
    arr_min[i][2] += min(arr_min[i+1][1], arr_min[i+1][2])

print(max(arr_max[0]), min(arr_min[0]))








# dp_max = [[0]*3 for _ in range(n)]
# dp_min = [[0]*3 for _ in range(n)]

# for i in range(n-2,-1,-1):
#     dp_max[i][0] = dp_max[i+1][0] + arr[i][0] + max(arr[i+1][0], arr[i+1][1])
#     dp_min[i][0] = dp_min[i+1][0] + arr[i][0] + min(arr[i+1][0], arr[i+1][1])

#     dp_max[i][1] = dp_max[i+1][1] + arr[i][1] + max(arr[i+1][0], arr[i+1][1], arr[i+1][2])
#     dp_min[i][1] = dp_min[i+1][1] + arr[i][1] + min(arr[i+1][0], arr[i+1][1], arr[i+1][2])

#     dp_max[i][2] = dp_max[i+1][2] + arr[i][2] + max(arr[i+1][1], arr[i+1][2])
#     dp_min[i][2] = dp_min[i+1][2] + arr[i][2] + min(arr[i+1][1], arr[i+1][2])

# print(dp_max[0])
# print(dp_min[0])