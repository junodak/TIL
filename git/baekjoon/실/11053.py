n = int(input())  # (168ms)
a = list(map(int, input().split()))

seq = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            seq[i] = max(seq[i], seq[j]+1)

print(seq)

# 11053 - 1 (108ms)
# n = int(input())
# a = list(map(int, input().split()))
# dp = [1]*n
# for i in range(1, n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]+1:
#             dp[i] = dp[j]+1
# print(max(dp))

# 11053 - 2 (48ms)
# n = int(input())
# a = list(map(int, input().split()))
# dp = [0]*1001
# for i in a:
#     dp[i] = max(dp[:i])+1
# print(max(dp))

# 11053 - 3 (40ms)
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
