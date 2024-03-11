# # 11053 - 1 (108ms)
# n = int(input())
# a = list(map(int, input().split()))
# dp = [1]*n
# for i in range(1, n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]+1:
#             dp[i] = dp[j]+1
# print(max(dp))

# # 11053 - 2 (48ms)
# n = int(input())
# a = list(map(int, input().split()))
# dp = [0]*1001
# for i in a:
#     dp[i] = max(dp[:i])+1
# print(max(dp))

# # 11053 - 3 (40ms)
# input()
# d = [0]
# for i in map(int, input().split()):
#     if i > d[-1]:
#         d.append(i)
#     else:
#         j = 0
#         while i > d[j]:
#             j += 1
#         d[j] = i
# print(len(d)-1)


# # 12015 - 1 (3736ms)
# input()
# d = [0]
# for i in map(int, input().split()):
#     if i > d[-1]:
#         d.append(i)
#     else:
#         start = 0
#         end = len(d)-1
#         while start <= end:
#             mid = (start + end)//2
#             if d[mid] < i:
#                 start = mid+1
#             else:
#                 end = mid-1
#         d[start] = i
# print(len(d)-1)


# # 12015 - 2(848ms)
# import bisect
# input()
# d = [-1000000001]
# p = []
# a = list(map(int, input().split()))
# for i in a:
#     if i > d[-1]:
#         d.append(i)
#         p.append(i)
#     else:
#         d[bisect.bisect_left(d, i)] = i
# print(len(d)-1)
# print(*p)



import bisect

n = int(input())
d = [-10**9-1]
a = list(map(int, input().split()))
q = []
for i in a:
    if i > d[-1]:
        d.append(i)
        q.append(len(d)-1)
    else:
        idx = bisect.bisect_left(d, i)
        d[idx] = i
        q.append(idx)

length = len(d)-1
n -= 1
max_n = 10**9+1
res = []
print(length)
while n >= 0:
    if q[n] == length:
        if a[n] < max_n:
            res.append(a[n])
            length -= 1
    n -= 1
res.reverse()
print(*res)

# 2
# 0 -1

# 2
# 1 1

# 2
# 1 2

# 3
# -1 0 1

# 3
# 3 1 2

# 3
# 4 3 2

# 4
# 1 5 10 4

# 4
# 1 3 3 2

# 4
# 1 10 100 9

# 4
# 100 20 30 40

# 4
# 10 20 30 5

# 5
# 1 3 5 2 6

# 5
# 2 1 1 0 2

# 5
# 1 10 100 1000 5

# 6
# 12 10 10 10 10 12

# 6
# 1 3 4 5 2 4

# 6
# 1 3 4 5 2 3

# 6
# 1 3 5 7 2 3

# 6
# 71 0 -1 20 1 50

# 7
# 10 30 5 7 50 9 15

# 7
# 2 3 4 1 2 3 4

# 7
# 1 3 7 8 5 4 2

# 8
# 15 14 14 14 14 15 14 14

# 9
# 3 1 4 6 2 2 0 3 6

# 10
# 10 9 8 7 6 5 4 3 2 1

# 10
# 2 -8 6 -2 3 -2 7 7 -8 -9

# 10
# -61 -28 -72 59 13 -21 84 -76 -52 -1

# 10
# 6 -21 85 -53 -9 32 -30 57 62 93

# 10
# 3 2 7 8 6 1 5 2 1 4

# 16
# -60 -41 -100 8 -8 -52 -62 -61 -76 -52 -52 14 -11 -2 -54 46
