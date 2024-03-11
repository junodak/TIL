import math
n = int(input())
arr = list(map(int, input().split()))*2
for i in range(n*2-1):
    arr[i+1] += arr[i]
cnt = 0
for i in range(n):
    for j in range(i,n+i):
        sum = arr[j]-arr[i]
        if sum<0:
            cnt += math.ceil(-sum/arr[n-1])
print(cnt)

# 1 -2 -1 3
# 1 -2 -1 3 1 -2 -1 3

# (-2), (-1)
# (1, -2), (-2, -1)
# (1, -2, -1)
# (-2, -1, 3, 1, -2)
# (-2, -1, 3, 1, -2, -1)
# (1, -2, -1, 3, 1, -2, -1)
# (-2, -1, 3, 1, -2, -1, 3, 1, -2, -1)

# 1 : (1, -2), (1, -2, -1), (1, -2, -1, 3, 1, -2, -1)
# -2 : (-2), (-2, -1), (-2, -1, 3, 1, -2), (-2, -1, 3, 1, -2, -1), (-2, -1, 3, 1, -2, -1, 3, 1, -2, -1)
# -1 : (-1)
# 3 : X

# 1 : -1, -2 / -1
# -2 : -2, -3 / -1, -2 / -1
# -1 : -1
# 3 : X



# n = int(input())
# a = list(map(int, input().split()))
# cnt = 0
# while min(a) < 0:
#     for i in range(n):
#         if a[i] < 0:
#             a[i] = -a[i]
#             a[(i + 1) % n] -= a[i]
#             a[(i - 1 + n) % n] -= a[i]
#             cnt += 1
# print(cnt)



# n = int(input())
# a = list(map(int, input().split()))
# cnt = 0
# i = a.index(min(a))

# while a[i] < 0:
#     a[i] = -a[i]
#     a[(i + 1) % n] -= a[i]
#     a[(i - 1 + n) % n] -= a[i]
#     i = a.index(min(a))
#     cnt += 1

# print(cnt)